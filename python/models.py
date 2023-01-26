from python import db


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
    Residents_Optional_Comment = db.Column(db.VARCHAR(3000), unique=False, nullable=True)
    Admins_Optional_Comment = db.Column(db.VARCHAR(3000), unique=False, nullable=True)

    def __repr__(self):
        return '<Receipt %r>' % self.Receipt_ID


class Users(db.Model):
    User_ID = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Password = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    Role = db.Column(db.VARCHAR(50), unique=False, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.Users_ID
