'''
Venue Views Module
'''
from django.db.models.expressions import RawSQL
from django.core.paginator import Paginator

from django.contrib.gis.db.models.functions import Distance as DistanceMeasure
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point

from rest_framework.exceptions import APIException, ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import VenueSerializer
from .forms import GetVenueForm
from .models import Venue

import requests
import re


# pylint:disable=no-self-use
# pylint:disable=no-member


# Define defaults for when a query returns no results.
# These coordinates are the centre of Bristol, with a 50km radius.
DEFAULT_LAT, DEFAULT_LNG, DEFAULT_RADIUS = 51.4545, -2.5879, 50000


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
    (default 1000)
    Distance, in meters, from a provided location in which to search for venues. Use in combination with the coordinates or postcode parameter.
    Example: search_radius=5000

    coordinates: str
    A string containing latitude & longitude - in that order.
    The venues in the response are sorted by distance from the coordinate.
    Example: coordinates=51.4545,-2.5879

    postcode: str
    A valid UK postcode. This is translated to latitude & longitude via a 3rd party. All validation is done by this external service.
    Errors will be returned in a 400 Bad Request, with a message in the body's 'detail' attribute.
    The venues in the response are sorted by distance from the coordinate.
    Examples: postcode=BS1 6AE, postcode=bs16ae
    Error response 1 - invalid postcode syntax:
    {"detail": "No matching postcode area, postcode district, postcode sector, or unit postcode found."}
    Error response 1 - correct syntax, no postcode:
    {"detail": "No matching postcode found."}

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

        # Get the radius parameter.
        radius = int(data["search_radius"])

        # Query for the venues.
        queryset = Venue.objects.filter(show_on_website=True)

        # Filter the results.
        if "business_type" in data:
            queryset = queryset.filter(business_type__label=data["business_type"])

        if "coordinates" in data:
            # Pull coordinates & radius from the query.
            lat, lng = map(float, data["coordinates"].split(","))
            queryset = query_by_distance(lat, lng, radius, queryset)

        elif "postcode" in data:
            postcode = data["postcode"]

            # Validate the postcode using a government-provided regular expression.
            if not re.match("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})", postcode):
                raise ParseError("Please enter a valid postocde")

            # Query for the coordinates.
            response = requests.get(f"http://api.getthedata.com/postcode/{postcode}").json()
            if "error" in response:
                error = response["error"]

                # Handle the API error.
                if error == "No matching postcode area, postcode district, postcode sector, or unit postcode found." \
                or error == "No matching postcode found.":
                    raise ParseError("Please enter a valid postcode")
                else:
                    raise APIException(error)

            # Ensure the response has the necessary data.
            if "data" not in response:
                raise APIException("Key 'data' missing from postcode lookup API")
            for key in ["latitude", "longitude"]:
                if key not in response["data"]:
                    raise APIException(f"Key 'data.{key}' missing from postcode lookup API")

            # Pull coordinates from the response.
            lat = float(response["data"]["latitude"])
            lng = float(response["data"]["longitude"])
            queryset = query_by_distance(lat, lng, radius, queryset)
        
        # Ensure there are results to display on the website,
        # even if the filters (e.g. location, distance) have removed any matches.
        found_venues = len(queryset) > 0
        if not found_venues:
            queryset = query_by_distance(
                DEFAULT_LAT, DEFAULT_LNG, DEFAULT_RADIUS, 
                Venue.objects.filter(show_on_website=True))

        # Paginate the results.
        results = Paginator(queryset, data["limit"]).page(data["offset"])

        # Serialize the results.
        serializer = VenueSerializer(results, many=True)

        # Return the results.
        # return Response({"found_venues": found_venues, "venues": serializer.data})
        return Response(serializer.data)

def query_by_distance(lat, lng, radius, queryset):
    point = Point(lng, lat)
    return queryset.filter(location__distance_lt=(point, Distance(m=radius))) \
                   .annotate(distance=DistanceMeasure("location", point)) \
                   .order_by("distance")
