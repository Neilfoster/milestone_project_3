import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestoneproject3me'
app.config["MONGO_URI"] = os.environ.get('mongo_uri')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_activities')
def get_activities():
    return render_template("home.html", 
    activities=mongo.db.Activities.find())
    
@app.route('/activity_view', methods=['POST', 'GET'])
def activity_view():
    return render_template('activity_view.html',
        #activities=mongo.db.Activities.find().limit(6), 
        ages=mongo.db.ages.find(),
        durations=mongo.db.duration.find(),
        user_supplied_age_group = request.GET['age_group'],
        user_supplied_activity_duration = request.GET['activity_duration'],
        activities = mongo.db.Activities.find(
               {'age_group': user_supplied_age_group,
                 'activity_duration': user_supplied_activity_duration,
               }))
   
    
    
@app.route('/add_activity', methods=['POST', 'GET'])
def add_activity():
    return render_template('add_activity.html',
    ages=mongo.db.ages.find(),
    durations=mongo.db.duration.find())

@app.route('/insert_activity', methods=['POST'])
def insert_activity():
    activities=mongo.db.Activities
    activities.insert_one(request.form.to_dict())
    return redirect(url_for('activity_view'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
