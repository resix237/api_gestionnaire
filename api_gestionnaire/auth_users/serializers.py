from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password


class UserGestionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.UserGestion
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value: str) -> str:
        return make_password(value)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_active'] = user.is_active
        token['is_staff'] = user.is_staff
        return token
