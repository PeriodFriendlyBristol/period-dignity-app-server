'''
Venue Views Module
'''

from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Venue
from .serializers import VenueSerializer

# pylint:disable=no-self-use
# pylint:disable=no-member


class VenueApi(APIView):
    '''
    # URL params
    `limit=5` 
    `offset=2`


    '''

    def get(self, request):
        '''
        the GET method endpoint for /api/venue
        '''
        url_params = request.GET
        print(url_params)
        queryset = Venue.objects.all()
        serializer = VenueSerializer(queryset, many=True)

        return Response(serializer.data)
