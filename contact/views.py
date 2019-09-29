
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Venue


# Create your views here.

class ContactsApi(APIView):
    '''
    The Docs go here
    '''
    def get(self, request):
        queryset = Venue.get.all()
        data = {'phone': 071234 }
        return Response(data)

