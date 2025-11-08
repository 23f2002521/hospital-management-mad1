from app import app
from flask_sqlalchemy import SQLAlchemy
from backend.models import *
from sqlalchemy.exc import IntegrityError
from flask import Flask, render_template,redirect,request,url_for
from flask_login import login_user , login_required,current_user
#app = Flask(__name__)


@app.route('/')
def home_v():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        admin = db.session.query(Admin).filter_by(email=email, password=password).first()
        if admin:
            login_user(admin)
            return redirect(f"/adashboard")

        user = db.session.query(Patient).filter_by(email=email, password=password).first()
        if user:
            login_user(user)
            return redirect(f"/pdashboard")

        doctor = db.session.query(Doctor).filter_by(email=email, password=password).first()
        if doctor:
            login_user(doctor)
            return redirect(f"/ddashboard")

        return "Invalid password or email"

      
@app.route('/register',methods=["GET","POST"])
def register():
    if request.method =="POST":
        u_name = request.form.get("cust_name")
        u_email = request.form.get("email")
        u_password = request.form.get("password")
        cust = db.session.query(Patient).filter_by(email=u_email).first()
        if not cust:
            cust = Patient(name=u_name,email=u_email,password=u_password)
            db.session.add(cust)
            db.session.commit()
            return redirect(url_for('login_page'))
        else:
            return "email already exist"
    return render_template("patient/register.html")  

@app.route('/adashboard' , methods=["GET" , "POST"])
@login_required
def admin_dashboard():
    
    return render_template("adashboard.html",current_admin=current_user)
    


@app.route('/pdashboard' , methods=["GET" , "POST"])
@login_required
def user_dashboard():
   
    return render_template("pdashboard.html",current_userr=current_user)
   
@app.route('/ddashboard' , methods=["GET" , "POST"])
@login_required
def doctor_dashboard():
    
    return render_template("ddashboard.html", current_doctor=current_user)
    
