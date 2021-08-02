from flask import Flask, render_template, request 
import pymongo

app = Flask(__name__)

# Routes
from user import routes

# Database
CONNECTION_STRING = "mongodb+srv://Hussar:Hussar1@hussarcluster.cokdm.mongodb.net/test"

client = pymongo.MongoClient(CONNECTION_STRING)
db = pymongo.database.Database(client, 'abobus')
user_collection = pymongo.collection.Collection(db,'bobabo')

@app.route('/send_here', methods = ['POST'])
def sendtodb():
    data = request.get_json()
    userName = data.get('username','')
    userPassword = data.get('password','')
    userEmail = data.get('email','')
    userFirstName = data.get('firstName','')
    userLastName = data.get('lastName','')
    db.bobobus.insert_one({"userName":userName,"userPassword":userPassword,"userEmail":userEmail,"userFirstName":userFirstName,"userLastName":userLastName})
    return "Sent to db " 


@app.route('/create')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


@app.route("/write")
def write():
    db.bobobus.insert_one({"name": "Bob"})
    return "Vse chetko"


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()