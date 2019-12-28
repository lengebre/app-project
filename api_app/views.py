from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api_app import serializers
# Create your views here.

class HelloApiView(APIView):
    """
    Test APIView.
    """
    serializer_class = serializers.HelloSerializer 

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
    def post(self, request):
      """ 
      Create a 'Hello' message with your name
      """
      serializers = self.serializer_class(data=request.data)
      # validate the input as per the specification of the serializer field
      
      if serializers.is_valid():
        name = serializers.validated_data.get('name')
        message = f'Hello, {name}'
        return Response({'message': message})
      else:
        return Response(
          serializers.errors, 
          status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):
      """ Handle updating an object """
      # update an object. Make a request to update the entire object
      # this returns a standard response
      return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
      """ Handle a partial update """
      # only update the field provided in the request
      return Response({'method': 'PATCH'})
    
    def delete(self, requerst, pk=None):
      """ Delete object """
      return Response({'method': 'DELETE'})