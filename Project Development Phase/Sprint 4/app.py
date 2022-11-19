from flask import Flask,render_template,request,url_for,redirect


from flask import Flask, render_template

app = Flask(__name__)



print("Db connected")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlogin',methods=['POST','GET'])
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/adminreg',methods=['POST','GET'])
def adminreg():
    
        
    return render_template('adminreg.html')


@app.route('/donlogin',methods=['POST','GET'])
def donlogin():
    return render_template('donlogin.html')

@app.route('/donregistration',methods=['POST','GET'])
def donregistration():
    
        
    return render_template('donregistration.html')

@app.route('/recipregistration',methods=['POST','GET'])
def recipregistration():
    return render_template('recipregistration.html')

@app.route('/reclogin',methods=['POST','GET'])
def reclogin():
    return render_template('reclogin.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)