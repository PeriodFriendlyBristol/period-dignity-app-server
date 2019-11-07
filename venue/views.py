'''
Venue Views Module
'''

from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.views import APIView


from .models import Venue
from .serializers import VenueSerializer

# pylint:disable=no-self-use
# pylint:disable=no-member


class VenueApi(APIView):
    '''
    # URL params
    `limit=20`
    `offset=1`
    '''

    def get(self, request):
        '''
        the GET method endpoint for /api/venue
        '''
        # Get the query parameters.
        print(request.GET)
        limit = request.GET.get('limit', 20)
        offset = request.GET.get('offset', 1)

        # Query for the venues.
        queryset = Venue.objects.all()

        # Paginate the results.
        paginator = Paginator(queryset, limit)
        serializer = VenueSerializer(paginator.page(offset), many=True)

        # Return the results.
        return Response(serializer.data)
