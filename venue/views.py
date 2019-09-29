
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class VenueApi(APIView):
    def get(self, request):
        data = {'location': 'BTP'}
        return Response(data)
