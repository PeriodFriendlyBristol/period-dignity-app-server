'''
Venue Views Module
'''
from django.db.models.expressions import RawSQL
from django.core.paginator import Paginator

from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import VenueSerializer
from .forms import GetVenueForm
from .models import Venue

from math import cos, pi

# pylint:disable=no-self-use
# pylint:disable=no-member


class VenueApi(APIView):
    '''
    Available query parameters:

    limit: int 
    (default 20)
    The maximum number of venues to return.
    Example: limit=50

    offset: int 
    (default 1)
    Used to paginate through results.
    Example: offset=5

    search_radius: int
    (default 5000)
    Distance, in meters, from a provided location in which to search for venues. Use in combination with the coordinates or postcode parameter.
    Example: search_radius=1000

    coordinates: str
    A string containing latitude & longitude - in that order.
    Example: coordinates=51.4545,-2.5879

    business_type: Community Centre | Public Toilet | Other | Youth Club | Foodbank | Library | Health Centre | GP 
    Filter the venues by venue type.
    Example: business_type=Youth Club
    '''

    def get(self, request):
        '''
        the GET method endpoint for /api/venue
        '''
        # Define parameter defaults.
        data = {"limit": 20, "offset": 1, "search_radius": 1000}

        # Update the defaults with the query parameters.
        data.update(request.GET.dict())

        # Validate the parameters.
        form = GetVenueForm(data)
        if not form.is_valid():
            raise ParseError(form.errors)

        # Query for the venues.
        queryset = Venue.objects.all()

        # Filter the results.
        if "business_type" in data:
            queryset = queryset.filter(business_type__label=data["business_type"])
        
        if "coordinates" in data:
            radius = int(data["search_radius"])
            lat, lng = map(float, data["coordinates"].split(","))
            queryset = get_nearby_venues(lat, lng, radius)

        # Paginate the results.
        results = Paginator(queryset, data["limit"]).page(data["offset"])

        # Serialize the results.
        serializer = VenueSerializer(results, many=True)

        # Return the results.
        return Response(serializer.data)

def meters_to_degrees(meters, latitude):
    return meters / (111.32 * 1000 * cos(latitude * (pi / 180)))

def get_nearby_venues(latitude, longitude, radius):
    """
    Return venues sorted by distance to specified coordinates
    whose distance is less than radius away, given in meters.
    """
    # Generage the great circle distance formula.
    gcd_formula = "6371 * acos(least(greatest(\
    cos(radians(%s)) * cos(radians(latitude)) \
    * cos(radians(longitude) - radians(%s)) + \
    sin(radians(%s)) * sin(radians(latitude)) \
    , -1), 1))"
    distance_raw_sql = RawSQL(gcd_formula, (latitude, longitude, latitude))

    # Compute the distances against each venue.
    queryset = Venue.objects.all().annotate(distance=distance_raw_sql).order_by('distance')

    # Filter results by radius.
    queryset = queryset.filter(distance__lt=radius/1000)
    return queryset
