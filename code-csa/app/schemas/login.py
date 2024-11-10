import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask, render_template, request, flash, redirect,url_for
from firebase_admin import firestore
import os

cred = credentials.Certificate('path/to/serviceAccount.json')
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'html_files'))
firebase_admin.initialize_app(cred)
db = firestore.client()

app.secret_key = 'anystringyouwant'

#Fetch email and password and check if it matches to database
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_ref = db.collection('users').document(email)
        user_doc = user_ref.get()
        
        if user_doc.exists:
            stored_password = user_doc.to_dict()['Password']
            
            if stored_password == password:
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Incorrect password.', 'error')
    else:
        flash('User does not exist.', 'error')
                
            

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
