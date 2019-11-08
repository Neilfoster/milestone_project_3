import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

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
        # Should decide what the default is, and assign it here, in case user
        # submits form without making a choice.
        # request.form.get('age_group', default_value)
        
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


    # Paginate activities before rendering template
    activity = mongo.db.Activities
    
    offset = 6
    limit = 6
    
    starting_id = activity.find().sort('_id', pymongo.ASCENDING)
    last_id = starting_id[offset]['_id']
     
    activities = activity.find({'_id': {'$gte' : last_id}}).sort('_id', pymongo.ASCENDING).limit(limit)
    
    output = []
    
    for i in activities:
        output.append({'activity' : i['activity_name'], 'age group:' : i['age_group'],
                       'duration' : i['activity_duration'],'details' : i['details'],
                       'equipment' : i['equipment']})
        
    next_url = '/activities?limit=' + str(limit) + '&offset=' + str(offset + limit)
    prev_url = '/activities?limit=' + str(limit) + '&offset=' + str(offset - limit)
        
    return jsonify({'result': output, 'prev_url': prev_url, 'next_url': next_url})



    return render_template('activity_view.html', ages=ages , durations=durations, activities=activities)
    
    
@app.route('/add_activity', methods=['POST', 'GET'])
def add_activity():
    '''
    Route for adding an activity 
    '''
    return render_template('add_activity.html',
    ages=mongo.db.ages.find(),
    durations=mongo.db.duration.find())

@app.route('/insert_activity', methods=['POST'])
def insert_activity():
    '''
    Route for Activity added
    '''
    activities=mongo.db.Activities
    activities.insert_one(request.form.to_dict())
    return redirect(url_for('activity_view'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
