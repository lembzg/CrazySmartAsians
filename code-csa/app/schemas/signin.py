import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask, render_template, request, flash
from firebase_admin import firestore
import os

cred = credentials.Certificate('path/to/serviceAccount.json')
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'html_files'))
firebase_admin.initialize_app(cred)
db = firestore.client()

app.secret_key = 'anystringyouwant'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']
        dob = request.form['date']
        if password == repassword:
            users_ref = db.collection('users')
            users_ref.add({
                'email': email,
                'password': password,
                'dob': dob 
                })
            return f'User {email} stored in database'

        else:
            flash('Passwords does not match!', 'error')

