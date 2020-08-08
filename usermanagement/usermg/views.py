from django.shortcuts import render
from .models import UserDetails, ActivityDetails
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# Basic function view to check whether application is up
def app_status(request):
    return render(request, 'usermg/welcome.html')


class ExtractData(APIView):
    """
    This is called when usermg/data is present in url.
    This extracts all the info from UserDetails model and for each user activity details are
    extracted from ActivityDetails model

    The response is a dictionary which shows all the user details
    Models are loaded from Django admin page
    """

    def __init__(self):
        super(ExtractData, self).__init__()

    def get(self, request):
        # extract all the user details from user model
        user = UserDetails.objects.all().values()
        output_details = []

        # for each user creating a user_dict dictionary and storing in output_details list
        for user_details in user:
            user_dict = {}
            activity_details = []
            user_dict['id'] = user_details['user_id']
            user_dict['real_name'] = user_details['name']
            user_dict['tz'] = user_details['time_zone']

            # extracting activity details for each user
            for activity in ActivityDetails.objects.filter(user_id=user_details['user_id']).values():
                activity_dict = {'start_time': activity['activity_start'].strftime('%b %d %Y %I:%M%p'), 'end_time': activity['activity_end'].strftime('%b %d %Y %I:%M%p')}
                activity_details.append(activity_dict)
            user_dict['activity_periods'] = activity_details
            output_details.append((user_dict))

        return Response({"ok": True, 'members': output_details}, status=status.HTTP_200_OK)