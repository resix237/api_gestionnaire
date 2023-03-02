from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'revenu', views.RevenuPersoViewset, basename='revenu perso')
router.register(r'depense', views.DepensePersoViewset,
                basename="depense perso")

router.register(r'categorieD', views.CategorieDepenseViewset,
                basename=" categorie D admin")
router.register(r'categorieR', views.CategorieRevenuViewset,
                basename="categorie R admin")
router.register(r'revenuAd', views.RevenuViewset, basename="revenu Ad")
router.register(r'depenseAd', views.DepenseViewset, basename="depense Ad ")
router.register(r'categorieDlist', views.CategorieDepenseList,
                basename="depense categorie")
router.register(r'categorieRlist', views.CategorieRevenuList,
                basename="revenu categorie")

urlpatterns = [
    path('', include(router.urls)),
]
