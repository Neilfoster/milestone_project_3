import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestoneproject3me'
app.config["MONGO_URI"] = os.environ.get('mongo_uri')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def get_activities():
    return render_template("home.html", activities=mongo.db.Activities.find())
    
@app.route('/activity_view')
def activity_view():
    return render_template('activity_view.html',activities=mongo.db.Activities.find(), ages=mongo.db.ages.age_group.find())
 
@app.route('/add_activity')
def add_activity():
    return render_template('add_activity.html',activities=mongo.db.Activities.find(), ages=mongo.db.ages.age_group.find())
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)