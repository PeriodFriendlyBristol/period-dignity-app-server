
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact


# Create your views here.

class ContactApi(APIView):
    '''
    The Docs go here
    '''

    def get(self, request):
        #queryset = Venue.get.all()
        data = {'phone': '07123456789'}
        return Response(data)
