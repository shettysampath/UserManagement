# UserManagement
Django project with data retrieval API from User and activity model.

### Models :
UserDetails - Model created to store user details
  - user_id: Primary key for each user
  - name: Name of the user
  - time_zone: Time zone of user
 
ActivityDetails - Model created to store activity start and end date for each user
  - activity_id: Primary key for each activity
  - user_id: Foreign key which connects with UserDetails user_id
  - activity_start: Start time of user activity
  - activity_end: End time of user activity

The above model have been loaded with dummy data. To see the data we use ExtractData API. URL path is given below

### Views :
  - ExtractData(Class based view)
      Rest API which sends a json response with all the user details
    
    
Application is hosted on Heroku platform. The output json response of API can been seen at path - 'https://usermngmt.herokuapp.com/usermg/data'

