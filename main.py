from flask import Flask, render_template,request,redirect,url_for
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from config import config
import pyrebase


app = Flask(__name__)
cred = credentials.Certificate("static/js/app.json")
firebase=pyrebase.initialize_app(config)
database=firebase.database()
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def gfg():
    default_value = '0'
    global username
    username = request.form.get('username', default_value)
    password= request.form.get('password', default_value)
    print(list(database.child("users").get().val()))
    print(dict(database.child("users").child(username).get().val())['Password'])
    if username in list(database.child("users").get().val()) and password==dict(database.child("users").child(username).get().val())['Password']:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html',error="user not found")
        
@app.route("/fetch_data")
def fetch_data():
    user_data=dict(database.child("users").child(username).get().val())
    user_data['username']=username
    print(user_data)
    sensor_data=dict(database.child("Boards").child(int(user_data['Board id'])).get().val())
    data= [user_data,sensor_data]
    return data

def sign_up():
    return render_template("index.html")

@app.route("/sign-up")
def sign_up():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",data=fetch_data())

if __name__=="__main__":
    app.run(debug=True)