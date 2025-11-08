from flask import Flask,render_template,redirect
from backend.models import db,Admin,Doctor,Patient,Appointment,Treatment,Department
from datetime import date,time
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
    db.init_app(app)
    app.config["SECRET_KEY"]="heyitsmeagain"
    login_manager=LoginManager(app)
    @login_manager.user_loader
    def load_user(email):
        return db.session.query(Admin).filter_by(email=email).first() or \
        db.session.query(Doctor).filter_by(email=email).first() or \
        db.session.query(Patient).filter_by(email=email).first() 
        
    app.app_context().push()
        #db.drop_all()
    db.create_all()
    return app

app = create_app()



from backend.initial_db import *

from routes import *

if __name__=="__main__":
    app.run(debug=True)

