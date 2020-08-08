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
  
### Views :
  - ExtractData
    Rest API which sends a json response with all the user details
