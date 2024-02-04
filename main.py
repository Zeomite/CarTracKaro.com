from flask import Flask, render_template, request, redirect, url_for
from collections.abc import MutableMapping
import firebase_admin
from firebase_admin import credentials, db
from config import config
import os 
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
print(config)
cred = credentials.Certificate(config)
firebase = firebase_admin.initialize_app(cred)
database = db.reference('/', url= os.environ.get('DB_URL'))

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def gfg():
    try:
        default_value = '0'
        global username
        username = request.form.get('username', default_value)
        password = request.form.get('password', default_value)

        users_data = database.child("users").get()

        if username in users_data and password == users_data[username]['Password']:
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', error="User not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return render_template('index.html', error="An unexpected error occurred. Please try again later.")

@app.route("/fetch_data")
def fetch_data():
    try:
        user_data = dict(database.child("users").child(username).get())
        user_data['username'] = username
        sensor_data = dict(database.child("Boards").child(str(user_data['Board id'])).get())
        data = [user_data, sensor_data]
        return data
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "An unexpected error occurred. Please try again later."

@app.route("/sign-up")
def sign_up():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    try:
        return render_template("dashboard.html", data=fetch_data())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return render_template('dashboard.html', error="An unexpected error occurred. Please try again later.")

if __name__ == "__main__":
    app.run(debug=True)
