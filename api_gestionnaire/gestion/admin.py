from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CategorieDepense)
admin.site.register(models.CategorieRevenu)
admin.site.register(models.Revenu)
admin.site.register(models.Depense)
