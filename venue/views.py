
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Venue


# Create your views here.

class VenueApi(APIView):
    '''
    the venue APi docs go here 
    '''
    def get(self, request):
        queryset = Venue.get.all()
        data = {'location': 'BTP'}
        return Response(data)
