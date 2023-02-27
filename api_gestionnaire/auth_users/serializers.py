from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from . import models


class UserGestionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.UserGestion
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     username = validated_data["username"]
    #     email = validated_data["email"]
    #     password = validated_data["password"]
    #     if (email and models.UserGestion.objects.filter(email=email).exclude(username=username).exists()):
    #         raise serializers.ValidationError(
    #             {"email": "Email addresses must be unique."})

    #     user = models.UserGestion(username=username, email=email)
    #     user.set_password(password)
    #     user.save()
    #     return user


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
