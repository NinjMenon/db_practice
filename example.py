from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask,request

connect("mongodb://localhost:27017/db_practice")

class Patient(MongoModel):
	name = fields.CharField()
	age  = fields.CharField()
	bmi = fields.CharField()

app = Flask(__name__)
     
@app.route("/new_patient", methods = ['POST'])
def add_patient():
	data = request.json
	for i in range(len(data)):
		p = Patient(name = data['name'], age = data['age'], bmi = data['bmi'])
		p.save()
	return("DONE")

@app.route("/average_bmi/<ag>")
def avg_bmi(ag):
	avg = []
	for patient in Patient.objects.raw({"age" : ag }):
		avg.append(ag)
	results = list(map(int, avg))
	return("{}".format(sum(results)/len(results)))	

			


