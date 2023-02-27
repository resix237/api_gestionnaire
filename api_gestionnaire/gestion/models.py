from django.db import models
from django.utils import timezone


class CategorieRevenu(models.Model):
    libelle = models.CharField(max_length=200, blank=False, unique=True)


class CategorieDepense(models.Model):
    libelle = models.CharField(max_length=200, blank=False, unique=True)

    class Meta:
        ordering = ['libelle']

    def __str__(self):
        return self.libelle


class Revenu(models.Model):
    montant = models.IntegerField(blank=False)
    date = models.DateField(auto_now_add=True)
    categorie = models.ForeignKey(
        "gestion.CategorieRevenu", on_delete=models.CASCADE)
    ower = models.ForeignKey(
        "auth_users.UserGestion", on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.date = timezone.now()
        return super(Revenu, self).save(*args, **kwargs)


class Depense(models.Model):
    montant = models.IntegerField(blank=False)
    date = models.DateField(auto_now_add=True)
    categorie = models.ForeignKey(
        "gestion.CategorieDepense", on_delete=models.CASCADE)
    ower = models.ForeignKey(
        "auth_users.UserGestion", on_delete=models.CASCADE)
