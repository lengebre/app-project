from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """
    Test APIView.
    """
    def get(self, request, format=None):
        """
        Returns a list of APIView features.GET retrieves a list of objects or

        a specific function.
        """
        an_apiview = [
          'Uses HTTP Methods as function (get, post, patch, put, delete)',
          'Is similar to a traditional Django View',
          'Gives you the most control over your application logic',
          'Is mapped amnually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
