from .models import db,Appointment,Admin,Department,Doctor,Patient,Treatment,date,time

if db.session.query(Admin).count()==0:
    admin=Admin(name="admin",email="admin@hospital.com",password="pass")
    db.session.add(admin)
    db.session.commit()

if db.session.query(Doctor).count()==0:
    doctor=Doctor(name="hayam",email="hayam@gmail.com",password="H1234567",dept_id=4)
    db.session.add(doctor)
    db.session.commit()
    doctor=Doctor(name="lia",email="lia@gmail.com",password="L1234567",dept_id=1)
    db.session.add(doctor)
    db.session.commit()
#db.session.query(Doctor).delete()
#db.session.commit()
if db.session.query(Patient).count()==0:
    patient=Patient(name="loyu",email="loyu@gmail.com",password="l123")
    db.session.add(patient)
    db.session.commit()
#db.session.query(Patient).delete()
#db.session.commit()
if db.session.query(Appointment).count()==0:
    appmnt=Appointment(pid=5,did=4,date=date(2025,11,20),time=time(10,10),status="completed")
    db.session.add(appmnt)
    db.session.commit()
#db.session.query(Appointment).delete()
#db.session.commit()

treatment=Treatment(aid=3,diagnosis="cough",prescription="paracetamol",notes="nil")
db.session.add(treatment)
db.session.commit()
#db.session.query(Treatment).delete()
#db.session.commit()






if db.session.query(Department).count()==0:
    patient=Department(dept_name="neuro",description="well im not a doc so idk",doctors_registered="sam,linda,kim")
    db.session.add(patient)
    db.session.commit()
#db.session.query(Department).delete()
#db.session.commit()


