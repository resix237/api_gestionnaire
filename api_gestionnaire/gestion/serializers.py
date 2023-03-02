from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models


class CategorieRevenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategorieRevenu
        fields = '__all__'


class CategorieDepenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategorieDepense
        fields = '__all__'


class RevenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Revenu
        fields = ("id", "montant", "categorie", "date")


class DepenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Depense
        fields = ("id", "montant", "categorie", "date")
