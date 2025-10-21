from flask import Flask
from backend.models import db,Admin,Doctor,Patient,Appointment,Treatment,Department
from datetime import date,time

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
    db.init_app(app)
    app.app_context().push()

    #db.drop_all()
    db.create_all()
    return app

app = create_app()

from backend.routes import *

from backend.initial_db import *



if __name__=="__main__":
    app.run(debug=True)

