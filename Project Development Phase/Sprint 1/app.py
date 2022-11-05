from flask import Flask,render_template,request,url_for,redirect

import ibm_db

dictionaryForEmailDonor={}
def printDonorData(conn):
    sql = "SELECT * FROM donorregistration"
    out = ibm_db.exec_immediate(conn, sql)
    document = ibm_db.fetch_assoc(out)
    while document != False:
        dictionaryForEmailDonor.update({document['EMAIL']:document['PASSWORD']})
        document = ibm_db.fetch_assoc(out)



def insertDonorData(conn,username,firstname,lastname,age,gender,blood,email,phonenumber,password,district,pincode):
    sql="INSERT INTO donorregistration(username,firstname,lastname,age,gender,blood,email,phonenumber,password,district,pincode) VALUES ('{}','{}','{}',{},'{}','{}','{}',{},'{}','{}',{})".format(username,firstname,lastname,age,gender,blood,email,phonenumber,password,district,pincode)
    out = ibm_db.exec_immediate(conn,sql)
    print('Number of affected rows : ',ibm_db.num_rows(out),"\n")




def deleteDonorData(conn,email):
    sql = "DELETE FROM donorregistration WHERE email={}".format(email)
    out = ibm_db.exec_immediate(conn, sql)
    print('Number of affected rows : ', ibm_db.num_rows(out), "\n")





try:
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=mnv62697;PWD=lQveCU2FkrD4mi5f;", "", "")
    print("Db connected")
except:
    print("Error")

app=Flask(__name__,template_folder='templates')



@app.route("/",methods=['POST','GET'])
def index():
    return render_template("indexpage.html")



 

@app.route("/donorlogin",methods=['POST','GET'])
def donorlogin():
    if request.method=="POST":
        printDonorData(conn)
        text=request.form['text']
        password=request.form['password']
        try:
            if dictionaryForEmailDonor[text] == password:
                return redirect(url_for('donorhome'))
        except:
            return "invalid email or password"
    return render_template("donorlogin.html")

@app.route("/donorregister",methods=['POST','GET'])
def donorregister():
    if request.method=="POST":
        username = request.form['username']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        gender=request.form['gender']
        age=request.form['age']
        blood=request.form['blood']
        email = request.form['email']
        phonenumber=request.form['phonenumber']
        district=request.form['district']
        pincode=request.form['pincode']
        password = request.form['password']
        insertDonorData(conn,username,firstname,lastname,age,gender,blood,email,phonenumber,password,district,pincode)
        
    return render_template('donorregister.html')

@app.route("/donorhome")
def donorhome():
    return "donor home page"



if __name__ == "__main__":
    app.run(debug=True)