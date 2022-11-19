from flask import Flask,render_template,request,url_for,redirect
from flask_mail import *
import ibm_db
from flask import Flask, render_template

app = Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=mnv62697;PWD=lQveCU2FkrD4mi5f";, '', '')

print("Db connected")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlogin',methods=['POST','GET'])
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/adminreg',methods=['POST','GET'])
def adminreg():
    if request.method=="POST":
        hospitalname = request.form['hospital-name']
        emailid = request.form['email']
        password = request.form['password']
        insert_sql = "INSERT INTO ADMINDETAILS VALUES (?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, hospitalname)
        ibm_db.bind_param(prep_stmt, 2, emailid)
        ibm_db.bind_param(prep_stmt, 3, password)
        ibm_db.execute(prep_stmt)
        
    return render_template('adminreg.html')


@app.route('/donlogin',methods=['POST','GET'])
def donlogin():
    return render_template('donlogin.html')

@app.route('/donregistration',methods=['POST','GET'])
def donregistration():
    if request.method=="POST":
        firstname=request.form['First_Name']
        lastname=request.form['Last_Name']
        dob=request.form['Birthday_day']
        gender=request.form['gender']
        age=request.form['age']
        blood=request.form['blood']
        email = request.form['email']
        phonenumber=request.form['phonenumber']
        district=request.form['district']
        pincode=request.form['pincode']
        password = request.form['password']
        insertDonorData(conn,username,firstname,lastname,age,gender,blood,email,phonenumber,password,district,pincode)
        
    return render_template('donregistration.html')

@app.route('/recipregistration',methods=['POST','GET'])
def recipregistration():
    return render_template('recipregistration.html')

@app.route('/reclogin',methods=['POST','GET'])
def reclogin():
    return render_template('reclogin.html')
if __name__ == "__main__":
    app.run(debug=True)




