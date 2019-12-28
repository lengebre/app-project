from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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

class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """
    # represents actions that you are going to perform
    serializer_class = serializers.HelloSerializer 

    def list(self, request):
        """ Return Hello Message """
        a_viewset = [
            'User actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello from viewset!', 'an_apiview': a_viewset})

    def create(self, request):
        """ Create a new hello message """
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handle getting an object by it's ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating and object """
        return Response ({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object """
        return Response ({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle the removing an object """
        return Response({'http_method': 'DELETE'})
      
