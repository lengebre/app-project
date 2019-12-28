from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """
    Serializer, a name field for testig the APIView
    """
    # Similar to Django Forms. Specify the fields to accepts
    # Takes care of validation rules
    name = serializers.CharField(max_length=10)
