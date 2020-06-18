from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from users.models import User


class UserSerializer(serializers.Serializer):
    # TODO: Ask why i need to indicate expliocity the fields ( in the other case it does alone)
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
	    model = User
	    fields = ['id', 'first_name', 'last_name', 'email']

    


    
    