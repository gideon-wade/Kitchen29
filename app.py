from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Kitchen29.db'
# Initialize the database
db = SQLAlchemy(app)


# Create db model
class Kitchen29(db.Model):
    Resident_Number = db.Column(db.Integer, primary_key=True)
    Resident_Name   = db.Column(db.String(50), nullable=False)
    Date_created    = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a function to return a string
    def __repr__(self):
        return '<Name %r>' % self.Resident_Number


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route("/add_receipt", methods=["POST", "GET"])
def add_receipt():
    if request.method == "POST":
        amount          = request.form["amount"]
        resident        = request.form["resident"]
        receipt_picture = request.form["receipt_picture"]
        return redirect(url_for("update_receipts", Amount=amount, Resident=resident, Receipt_picture=receipt_picture))
    else:
        return render_template("add_receipt.html")


@app.route("/half_annually_payment")
def half_annually_payment():
    return render_template("half_annually_payment.html")


@app.route("/receipts")
def receipts():
    return render_template("receipts.html")


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
