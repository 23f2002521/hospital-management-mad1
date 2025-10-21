from flask_sqlalchemy import SQLAlchemy
from datetime import date
from datetime import time
from sqlalchemy import UniqueConstraint
db=SQLAlchemy()

class Admin(db.Model):
    __tablename__="admin"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    

class Doctor(db.Model):
    __tablename__="doctor"
    did = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('department.Dept_id'), nullable=False)
    department = db.relationship('Department', backref='doctors')


class Patient(db.Model):
    __tablename__="patient"
    pid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    #appoinmt_details=db.Column(db
    # specialisation=db.Column(db.String,ForeignKey=("department.dept_name"),nullable=False)
    

class Appointment(db.Model):
    __tablename__="appmnt"
    aid=db.Column(db.Integer,autoincrement=True,primary_key=True)
    pid = db.Column(db.Integer)
    did = db.Column(db.Integer)
    date = db.Column(db.Date,nullable=False)
    time = db.Column(db.Time,nullable=False,unique=True)
    status=db.Column(db.String)
    __table_args__ = (
       db.UniqueConstraint('date', 'time', 'did', name='unique_appointment_slot'),
    )
    pid = db.Column(db.Integer, db.ForeignKey('patient.pid'), nullable=False)
    did = db.Column(db.Integer, db.ForeignKey('doctor.did'), nullable=False)
    patient = db.relationship('Patient', backref='appointments')
    doctor = db.relationship('Doctor', backref='appointments')
    #treatment=db.relationship('treatment',backref='treatmentss')

class Treatment(db.Model):
    __tablename__="treatment"
    tid=db.Column(db.Integer,autoincrement=True,primary_key=True)
    aid = db.Column(db.Integer, db.ForeignKey('appmnt.aid'), nullable=False)
    diagnosis=db.Column(db.String,nullable=False)
    prescription = db.Column(db.String,nullable=True)
    notes=db.Column(db.String)
    #appointment_id = db.Column(db.Integer, db.ForeignKey('appmnt.aid'), nullable=False)
    appointment = db.relationship('Appointment', backref='treatments')

class Department(db.Model):
    __tablename__="department"
    Dept_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    dept_name=db.Column(db.String,nullable=False)
    description=db.Column(db.String)
    doctors_registered=db.Column(db.String,nullable=False)
    
