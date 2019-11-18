 # Creative Kids
 
 Creative Kids is an app built with Flask And MongoDB.The aim of my project is to
 use the technologies I have learnt so far to create a simple yet effective app which
 allows users to create and view activities for kids.
 
 In this project I have used [Python](https://www.python.org/) along with the Python framework 
 [Flask](https://www.fullstackpython.com/flask.html),[MongoDB](https://www.mongodb.com/)
 (A document based database) and a css framework [Bootstrap](https://getbootstrap.com/) for
 layout and styling purposes.
 
 ## UX
 I wanted to create a simple but much needed app that could benefit parents when they 
 run out of ideas of how to keep their kids entertained and also to bond with them
 through play. The app is designed to allow users to create, manage and store ideas all 
 in one place. Is has a simple , bright and enegetic design scheme to make the app 
 intuitive and energetic. There is also a filter designed to pick only the age group and duration 
 that the user needs to avoid clutter. 
 
 ## User Stories 
 > As a user I would like to be able to view activities to bond wth my child
 
 > I need an app where I can share my ideas for play activities for children
 and be able to access them later. 
 
 > I would like to see an app where I can filter through activities by age group and
 lenght to avoid spending time searching through everything. 
 
 ## Wireframes
 [Desktop View](https://github.com/Neilfoster/milestone_project_3/tree/master/Docs/desktop_view)
 [Mobile View](https://github.com/Neilfoster/milestone_project_3/tree/master/Docs/mobile_view)
 
 ## Technology Used
 
 * [HTML5](https://en.wikipedia.org/wiki/HTML5)
 * [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
 * [Bootstrap](https://getbootstrap.com/)
 * [Python](https://www.python.org/)
 * [Flask](https://www.fullstackpython.com/flask.html)
 * [Javascript](https://www.javascript.com/)
 * [Jquery](https://jquery.com/)
 * [Font Awesome](https://fontawesome.com/)
 * [MongoDB](https://www.mongodb.com/)

 ## Database
 I used MongoDB for the database which I created myself. I linked my database to my 
 project using [PyMongo](https://api.mongodb.com/python/current/).This way I could 
 send and recieve data from my datbase with ease. 
 
 ## Things that I could improve
 
 I would like to evntually set up a login system with user profiles and the ability 
 to edit activities if they were previously made by the user. I would also 
 like to implement pagination as the website grows, I tried for this project but
 i was running out of time and thought it would be better to have a functioning 
 website than a non functioning one. 
 
 ## Testing
 
 Most of the testing was done during the development stage which was done manually.
 
 ### Testing Python
 Most of my python testing was done as I was writing the code. I would normally
 write a small function or statement and then test if it was working. I find small 
 manual tests as I go Along easier to mange as there is less room for error and 
 less code to go through to find the error.
 
 ### Database Testing 
 I tested the database anytime I made a call or request to see if the two were linked properly.
 I also tested the data base by using the forum in my app to add data to my MongoDB.
 
 ### Testing Flask Views
 I tested each Flask view as I went along. I would test my views after adding any new code 
 or funcionality to my views to make sure they rendered as expected. 
 
 ### Testing Matrix
 A test matrix was carried out to make sure all the elements of my app renedered 
 consistently across all different devices and browsers and that all functionality 
 performed as expected. you can find a copy of the test matrix [here](https://www.mongodb.com/)
 
 
 
 ## Rescource Websites used
 * Google Images
 * Font Awesome 
 
 
 ## Deployment 
 Making sure my application was ready for deployment involved the following steps.
 * Removing all my passwords and sensitive variables and replaced them with secret keys
 and variables.
 * Making sure the requirements.txt is up to date with all the latest packages.
 * Setting Flasks debugger to false
 * Making sure the procfile is inplace as it required by Heroku
 * Push all my latest code to GitHub ready for deployment via Heroku
 
  ## Content
  
  All content was made by myself , I used images from google images for the size
  of picture I wanted to use. 
 
 
  ## Credits & Acknowledgments
  
 I would like to thank the following people for their help and inspiration for my project
 * Mentor **Brian Macharia**
 * The Code institute **Tutor support Team**
 * Youtuber **Pretty Printed**
 * Youtuber **Travesty Media**