from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, generics, mixins
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from . import models
from . import serializers


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.ower == request.user

# ////:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


class CategorieDepenseList(viewsets.ModelViewSet):
    queryset = models.CategorieDepense.objects.all()
    serializer_class = serializers.CategorieDepenseSerializer
    permission_classes = (IsAuthenticated,)


class CategorieRevenuList(viewsets.ModelViewSet):
    queryset = models.CategorieRevenu.objects.all()
    serializer_class = serializers.CategorieRevenuSerializer
    permission_classes = (IsAuthenticated,)


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class CategorieRevenuViewset(viewsets.ModelViewSet):
    queryset = models.CategorieRevenu.objects.all()
    serializer_class = serializers.CategorieRevenuSerializer
    permission_classes = (IsAdminUser,)


class CategorieDepenseViewset(viewsets.ModelViewSet):
    queryset = models.CategorieDepense.objects.all()
    serializer_class = serializers.CategorieDepenseSerializer
    permission_classes = (IsAdminUser,)


class RevenuPersoViewset(viewsets.ModelViewSet):

    serializer_class = serializers.RevenuSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return models.Revenu.objects.filter(ower=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(ower=self.request.user)


class DepensePersoViewset(viewsets.ModelViewSet):

    serializer_class = serializers.DepenseSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return models.Depense.objects.filter(ower=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(ower=self.request.user)
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


class RevenuViewset(viewsets.ModelViewSet):
    queryset = models.Revenu.objects.all()
    serializer_class = serializers.RevenuSerializer
    permission_classes = (IsAdminUser,)


class DepenseViewset(viewsets.ModelViewSet):
    queryset = models.Depense.objects.all()
    serializer_class = serializers.RevenuSerializer
    permission_classes = (IsAdminUser,)
