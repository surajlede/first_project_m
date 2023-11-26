from flask import Flask,jsonify,request,render_template
import numpy as np
import config

from project_app.utils import MedicalInsurance

app = Flask(__name__)


@app.route('/',methods =['GET','POST']) 
def my_fun():
    
    return render_template('index.html')


@app.route("/predict_charges",methods = ['POST',"GET"])

def get_insurance_charges():


    data = request.form
    print("Data Is :",data)
    
    age = eval(data['age'])  
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges  = med_ins.get_predict_chagres()
    return jsonify({"insrance price": f"DEAR CUSTOMER ,YES You will get medical insurance Rupees {np.round(charges[0],2)} /-"})





app.run(port = config.PORT_NUMBER,debug = False ,host='0.0.0.0' ) 



