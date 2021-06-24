from flask import Flask, render_template, request
import pymongo
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET'])
def login():
    Email = request.args.get('email')
    Password = request.args.get('password')
    con = pymongo.MongoClient('localhost', 27017)
    db = con['mydb']
    col = db['mycol']
    data = {'Email': Email, 'Password': Password}
    col.insert_one(data)
    return render_template('index.html', msg='Login in done successfully')
app.run(debug=True)



