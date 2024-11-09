import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask
app = Flask(__name__)
app.secret_key = "anystringyouwant"

# Initialize Firebase
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Collection: users
class User:
    def __init__(self, email, username, password, dateofbirth):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.dateofbirth=dateofbirth

    def save(self):
        user_ref = db.collection('users').document(self.username)
        user_ref.set({
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'dateofbirth': self.dateofbirth
        })

    @staticmethod
    def get_user(username):
        user_ref = db.collection('users').document(username).get()
        return user_ref.to_dict() if user_ref.exists else None
    

# Collection: capsules
class Capsule:
    def __init__(self, name, password, time, user_id, viewlist):
        self.name = name
        self.password=generate_password_hash(password)
        self.time = time
        self.user_id = user_id
        self.viewlist=viewlist

    def save(self):
        capsule_ref = db.collection('capsules').add({
            'name': self.name,
            'password': self.location,
            'time': self.time,
            'user_id': self.user_id,
            'viewlist': self.viewlist,
        })

# Collection: messages
class Message:
    def __init__(self, type, date, time, location, user_id, capsule_id, content):
        self.type = type
        self.date= date
        self.time = time
        self.location= location
        self.user_id = user_id
        self.capsule_id= capsule_id
        self.content=content

    def save(self):
        capsule_ref = db.collection('messages').add({
            'type': self.type,
            'date': self.date,
            'time': self.time,
            'location': self.location,
            'user_id': self.user_id,
            'capsule_id': self.capsule_id,
            'content':self.content,
        })