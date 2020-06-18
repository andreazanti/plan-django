from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    # this is to exclude password
    # def to_representation(self, obj):
    #     rep = super(UserSerializer, self).to_representation(obj)
    #     rep.pop('password', None)
    #     return rep

    class Meta:
        model = User
        fields = '__all__'
