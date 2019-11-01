'''
Venue Views Module
'''

from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters


from .models import Venue
from .serializers import VenueSerializer

# pylint:disable=no-self-use
# pylint:disable=no-member


class VenueFilter(filters.FilterSet):
    class Meta:
        model = Venue
        fields = {
            'name': ['lt', 'gt'],
        }


class VenueApi(ListAPIView):
    '''
    # URL params
    `limit=5` 
    `offset=2`


    '''

    serializer_class = VenueSerializer

    def get_queryset(self):
        queryset = Venue.objects.all()
        return queryset

    # def get(self, request):
    #    '''
    #    the GET method endpoint for /api/venue
    #    '''
    #    url_params = request.GET
    #    print(url_params)

    #    return Response(serializer.data)
