'''
Venue Views Module
'''

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.views import APIView


from .models import Venue
from .serializers import VenueSerializer

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

    # Define the known venue types.
    business_types = ['Community Centre', 'Public Toilet', 'Other', 'Youth Club', 'Foodbank', 'Library', 'Health Centre', 'GP']

    def get(self, request):
        '''
        the GET method endpoint for /api/venue
        '''
        # Get the query parameters.
        print(request.GET)
        limit = request.GET.get('limit', 20)
        offset = request.GET.get('offset', 1)
        business_type = request.GET.get('business_type', None)

        # Validate the limit parameter.
        try:
            limit = int(limit)
        except:
            raise APIException("Parameter 'limit' must be an integer")
        if limit < 1:
            raise APIException("Parameter 'limit' must be above 0")

        # Validate the offset parameter.
        try:
            offset = int(offset)
        except:
            raise APIException("Parameter 'offset' must be an integer")
        if offset < 1:
            raise APIException("Parameter 'offset' must be above 0")

        # Filter the results.
        filtered = False

        # Check for business_type.
        if business_type:
            if business_type not in self.business_types:
                raise APIException(f"Parameter 'business_type' must be one of: {self.business_types}")
            queryset = Venue.objects.filter(business_type__label=business_type)
            filtered = True

        # Query for all venues if there are no filters.
        if not filtered:
            queryset = Venue.objects.all()

        # Paginate the results.
        paginator = Paginator(queryset, limit)
        serializer = VenueSerializer(paginator.page(offset), many=True)

        # Return the results.
        return Response(serializer.data)
