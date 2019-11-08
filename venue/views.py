'''
Venue Views Module
'''
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.views import APIView


from .serializers import VenueSerializer
from .forms import GetVenueForm
from .models import Venue

# pylint:disable=no-self-use
# pylint:disable=no-member


class VenueApi(APIView):
    '''
    Available query parameters:

    limit: int 
    (default 20)

    offset: int 
    (default 1)

    business_type: Community Centre | Public Toilet | Other | Youth Club | Foodbank | Library | Health Centre | GP 
    (default: None)
    '''

    def get(self, request):
        '''
        the GET method endpoint for /api/venue
        '''
        # Define parameter defaults.
        data = {"limit": 20, "offset": 1}

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

        # Paginate the results.
        paginator = Paginator(queryset, data["limit"])
        serializer = VenueSerializer(paginator.page(data["offset"]), many=True)

        # Return the results.
        return Response(serializer.data)
