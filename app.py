import sys

from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, engine
from sqlalchemy_utils import database_exists, create_database

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Gideon/PycharmProjects/Kitchen29/instance/Kitchen29.db'
# Initialize the database

db = SQLAlchemy(app)


# Object of the current state of half_annually_payment
class Residents(db.Model):
    Resident_Number = db.Column(db.Integer, primary_key=True)
    Resident_First_Name = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Resident_Last_Name = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Balance = db.Column(db.Numeric(5, 2), unique=False, nullable=False)

    def __repr__(self):
        return '<Resident %r>' % self.Resident_First_Number


class Receipts(db.Model):
    Receipt_ID = db.Column(db.Integer, primary_key=True)
    Receipts_Resident_Number = db.Column(db.Integer, unique=True, nullable=False)
    Amount = db.Column(db.Numeric(5, 2), unique=False, nullable=False)
    Date_Uploaded = db.Column(db.Date, unique=False, nullable=False)
    Approved = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return '<Receipt %r>' % self.Receipt_ID


# No idea why, but with this "with" shit create_all() works. I'll take it.
with app.app_context():
    print("Creating Database")
    db.create_all()


@app.route('/')
def home():  # put application's code here
    residents = Residents.query.all()
    return render_template("index.html", residents=residents)


@app.route("/add_receipt", methods=["POST", "GET"])
def add_receipt():
    residents = Residents.query.all()
    if request.method == "POST":
        amount = request.form["amount"]
        resident = request.form["resident"]
        receipt_picture = request.form["receipt_picture"]
        try:
            if amount is not "" and resident is not "" and receipt_picture is not "":
                print("We're in if*2 --------------------")
                print("amount: " + amount)
                print("resident: " + resident)
                print("receipt_picture: " + receipt_picture)
                print("We're in if*2 --------------------")
                return redirect(
                    url_for("update_receipts",
                            amount=amount,
                            resident=resident,
                            receipt_picture=receipt_picture))
        except:
            print("POST FAILED")
    else:
        return render_template("add_receipt.html", residents=residents)


@app.route("/half_annually_payment")
def half_annually_payment():
    residents = Residents.query.all()
    return render_template("half_annually_payment.html", residents=residents)


@app.route("/receipts")
def receipts():
    # A lit more complicated, but it basically does the
    # same but orders it with newest date first
    receipts = Receipts.query.order_by(Receipts.Date_Uploaded.desc()).all()
    return render_template("receipts.html", receipts=receipts)


@app.route("/receipts")
def update_receipts(amount, resident, receipt_picture):
    return render_template("receipts.html",
                           amount=amount,
                           resident=resident,
                           receipt_picture=receipt_picture)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/<resident>")
def choose_resident(resident):
    return render_template(f"Residents/{resident}.html")


if __name__ == '__main__':
    app.run(debug=True)
