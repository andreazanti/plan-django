from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from plan.apis.serializers import * 
from plan.models import Customer
# from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     token = Token.objects.create(user=user)
    #     return token