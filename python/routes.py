from flask import Blueprint, render_template, url_for, redirect, request, session
from python.models import *
from datetime import datetime
from python import db

routes = Blueprint('routes', __name__)


@routes.route('/')
def home():  # put application's code here
    residents = Residents.query.all()
    return render_template("index.html", residents=residents)





@routes.route("/add_receipt", methods=["POST", "GET"])
def add_receipt():
    residents = Residents.query.all()
    if request.method == "POST":
        amount = request.form["amount"]
        resident = request.form["resident"]
        receipt_picture = request.form["receipt_picture"]
        optional_receipt_comment = request.form["optional_receipt_comment"]
        if amount is not "" and resident is not "" and receipt_picture is not "":
            receipt = Receipts(Receipt_ID=Receipts.query.count() + 1,
                               Receipts_Resident_Number=resident,
                               Amount=amount,
                               Date_Uploaded=datetime.now().date(),
                               Approved=False,
                               Residents_Optional_Comment=optional_receipt_comment,
                               Admins_Optional_Comment="")
            db.session.add(receipt)
            db.session.commit()
            return redirect(url_for("routes.receipts"))
        else:
            # POST FAILED
            return render_template("add_receipt.html", residents=residents)
    else:
        return render_template("add_receipt.html", residents=residents)


@routes.route("/half_annually_payment")
def half_annually_payment():
    residents = Residents.query.all()
    return render_template("half_annually_payment.html", residents=residents)


@routes.route("/receipts")
def receipts():
    # A lit more complicated, but it basically does the
    # same but orders it with newest date first
    receipts = Receipts.query.order_by(Receipts.Date_Uploaded.desc()).all()
    residents = Residents.query.all()
    return render_template("receipts.html", receipts=receipts, residents=residents)


@routes.route("/update_admin_comment", methods=["POST"])
def update_admin_comment():
    if request.method == "POST":
        receipt_id = request.form["receipt_id"]
        admin_comment = request.form["admin_comment"]
        receipt = Receipts.query.filter_by(Receipt_ID=receipt_id).first()
        receipt.Admins_Optional_Comment = admin_comment
        db.session.commit()
    return redirect(url_for("routes.receipts"))


@routes.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            session['role'] = 'admin'
        elif username == "dev" and password == "dev":
            session['role'] = 'dev'
        else:
            session['role'] = 'regular'
        return redirect(url_for('routes.home'))
    else:
        return render_template("login.html")


@routes.route("/<resident>")
def choose_resident(resident):
    residents = Residents.query.all()
    return render_template(f"Residents/{resident}.html", residents=residents, resident=resident)
