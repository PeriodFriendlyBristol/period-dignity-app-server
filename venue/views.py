
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Venue


# Create your views here.

class VenueApi(APIView):
     '''
    the venue APi docs go here 
    '''
    def get(self, request):
        #queryset = Venue.get.all()
        data = {
            'location': 'BTP'
            'name': 'Boston Tea Party',
            'description': 'Independant Coffee Shop',
            'address_line_1': '302 Gloucester Road',
            'address_line_2': 'Gloucester Road',
            'address_line_3': 'Somewhere in Bristol',
            'city': 'Bristol',
            'postcode': 'BS7 8LQ',
            'country': 'England',

            'product_location': 'In the ladies toilets',
      #      'business_type': 1,
      #      'venue_status': 1,
      #      'social_media': 2,

            'toilet': True
            'stock': True
            'wheelchair_access': True

            'opening_hours': True, 
            'monday_open': '09:00',
            'monday_close': '22:00',
            'tuesday_open': '09:00',
            'tuesday_close': '22:00',
            'wednesday_open': '09:00',
            'wednesday_close': '22:00',
            'thursday_open': '09:00',
            'thursday_close': '22:00',
            'friday_open': '09:00',
            'friday_close': '22:00',
            'saturday_open': '09:00',
            'saturday_close': '22:00',
            'sunday_open': '11:00',
            'sunday_close': '17:00',




        }
        return Response(data)
