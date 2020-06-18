from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
	    model = User
	    fields = ['id', 'first_name', 'last_name', 'email']

    # TODO: Token is created but django raises an exception
    def create(self, validated_data):
        print("TEST")
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        print("USER")
        token = Token.objects.create(user = user)
        return token