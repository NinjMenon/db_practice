from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask,requests

connect("mongodb://vcm-1849.vm.duke.edu/db_practice")

class Patient(MongoModel):
	name = fields.CharField()
	age  = fields.CharField()
	bmi = fields.CharField()

app = Flask(__name__)
     
@app.route("/new_patient")
def add_patient():
	data = request.json()
	for i in range(len(data)):
		p = Patient(name = data['name'], age = data['age'], bmi = data['bmi'])
		p.save()

@app.route("/average_bmi/<age>")
def avg_bmi(age):
	avg = []
	for patient in Patient.objects.raw({"age" : age})
		avg.append(float(patient.bmi))
	return(avg.mean())
			


