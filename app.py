from flask import Flask,render_template,request,url_for,redirect,send_file,send_from_directory
from werkzeug.utils import secure_filename
import smtplib
import os
from flask.templating import render_template
from pro import generate_marksheet
from pro import concise_mrks
from pro import sendmail

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/Upload_files", methods=["POST"])
def upload():
    if request.method=="POST":
        for file in request.files:
         if not os.path.exists("sample_input"):
             os.mkdir('sample_input')        
         request.files[file].save('sample_input/'+file+'.csv')



         return render_template('index.html')
@app.route("/generatemarksheet", methods=["POST"])
def generating_marksheet():

    p = float(request.form['positive'])
    n = float(request.form['negative'])
    generate_marksheet(p,n)
        
    return redirect('/')
    


@app.route("/generateConciseMarksheet",methods=["POST"])
def creating_concisesheet():
    p = float(request.form['positive'])
    n = float(request.form['negative'])
    concise_mrks(p,n)
        
    
    return redirect('/')
@app.route("/sendmails",methods=["POST"])
def sendingmails():
    print("Hello from sendemail")
    sendmail()
    return redirect('/')
    
    
app.run(debug=True)