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
        return '<Resident %r>' % self.Resident_First_Name


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
    if request.method == "POST":
        try:
            amount = request.form["amount"]
            resident = request.form["resident"]
            receipt_picture = request.form["receipt_picture"]
            return redirect(
                url_for("update_receipts", Amount=amount, Resident=resident, Receipt_picture=receipt_picture))
        except:
            print("POST FAILED")

    else:
        return render_template("add_receipt.html")


@app.route("/half_annually_payment")
def half_annually_payment():
    residents = Residents.query.all()
    return render_template("half_annually_payment.html", residents=residents)


@app.route("/receipts")
def receipts():
    import pymysql
    import re
    host = 'localhost'
    user = 'root'
    password = ''
    try:
        connection = pymysql.connect(host=host, user=user, password=password, db=db, use_unicode=True, charset='utf-8')
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
    except Exception as e:
        sys.exit('error', e)

    cur = connection.curser()
    cur.execute("SELECT * FROM dataset")
    data = cur.fetchall()
    for row in data:
        id_berita = row[0]
        judul = row[1]
        isi = row[2]
        print('===============================================')
        print('BERITA KE', id_berita)
        print('Judul :', judul)
        print('Isi   :', isi)
        print('===============================================')

    return render_template("receipts.html", db=db)


@app.route("/receipts")
def update_receipts(Amount, Resident, Receipt_picture):
    return render_template("receipts.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/<resident>")
def choose_resident(resident):
    return render_template(f"Residents/{resident}.html")


if __name__ == '__main__':
    app.run(debug=True)
