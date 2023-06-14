from flask import Flask, render_template,request,redirect,url_for
from collections.abc import MutableMapping
import firebase_admin
from firebase_admin import credentials,db
from config import config



app = Flask(__name__)
cred = credentials.Certificate("static/js/app.json")
firebase=firebase_admin.initialize_app(cred)
database=db.reference('/',url='https://car-track-app-a01ae-default-rtdb.firebaseio.com/')

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def gfg():
    default_value = '0'
    global username
    username = request.form.get('username', default_value)
    password= request.form.get('password', default_value)
    if username in list(database.child("users").get()) and password==dict(database.child("users").child(username).get())['Password']:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html',error="user not found")
        
@app.route("/fetch_data")
def fetch_data():
    user_data=dict(database.child("users").child(username).get())
    user_data['username']=username
    sensor_data = dict(database.child("Boards").child(str(user_data['Board id'])).get())
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
