import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

# ENVIROMENT VARIABLES
app.config["MONGO_DBNAME"] = 'milestoneproject3me'
app.config["MONGO_URI"] = os.environ.get('mongo_uri')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_activities')
def get_activities():
    ''' 
    Route for Landing Page 
    '''
    return render_template("home.html", 
                            activities=mongo.db.Activities.find())
    

@app.route('/activity_view', methods=['POST', 'GET'])
def activity_view():
    '''
    Route For Activity page, Allows users to view all actvities,
    filterted activities and pagination
    '''
    ages = mongo.db.ages.find()
    durations = mongo.db.duration.find()

    # This will only happen if the user has selected age and duration restrictions
    if request.method == 'POST':
        user_supplied_age_group = request.form.get('age_group')
        user_supplied_activity_duration = request.form.get('activity_duration')

        activities = mongo.db.Activities.find(
               {
                'age_group': user_supplied_age_group,
                'activity_duration': user_supplied_activity_duration
               }
        )
    
    # This block gets executed the first time the user comes to the page.
    else:
        # Get all activities
        activities = mongo.db.Activities.find()


    return render_template('activity_view.html', ages=ages , durations=durations, activities=activities)
    
    
@app.route('/add_activity', methods=['POST', 'GET'])
def add_activity():
    '''
    Route for adding an activity 
    '''
    return render_template('add_activity.html',
                            ages = mongo.db.ages.find(),
                            durations = mongo.db.duration.find())

@app.route('/insert_activity', methods=['POST'])
def insert_activity():
    '''
    Route for Activity added
    '''
    activities=mongo.db.Activities
    activities.insert_one(request.form.to_dict())
    return redirect(url_for('activity_view'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5000')),
        debug=False)
        
