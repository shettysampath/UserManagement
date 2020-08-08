from django.db import models


# Model to store user details
class UserDetails(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    time_zone = models.CharField(max_length=200)

    class Meta:
        db_table = 'user_details'


# Model to store activity start and end time details.
class ActivityDetails(models.Model):
    activity_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    activity_start = models.DateTimeField()
    activity_end = models.DateTimeField()

    class Meta:
        db_table = 'activity_details'

