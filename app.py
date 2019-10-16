import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestoneproject3me'
app.config["MONGO_URI"] = os.environ.get('mongo_uri')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_activities')
def get_activities():
    return render_template("activities.html", activities=mongo.db.Activities.find())
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)