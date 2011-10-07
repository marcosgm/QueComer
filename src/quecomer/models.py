from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class TipoAlimento (models.Model):
    nombre = models.CharField(max_length=200)
    color = models.IntegerField()
    def __unicode__(self):
        return self.nombre


class Ingrediente (models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey('TipoAlimento')
    grCHidratox100 = models.IntegerField()
    grProteinax100 = models.IntegerField()
    grGrasax100 = models.IntegerField()
    kcalx100 = models.IntegerField()
    def __unicode__(self):
        return self.nombre

class Plato (models.Model):
    nombre = models.CharField(max_length=200)
    fotoUrl = models.CharField(max_length=200)
    ingrediente1 = models.ForeignKey('Ingrediente', related_name='ing1')
    ingrediente2 = models.ForeignKey('Ingrediente', related_name='ing2')
    ratio_ing1 = models.IntegerField()
    ratio_ing2 = models.IntegerField()
    gramos = models.IntegerField()
    kcal = models.IntegerField()
#    foto = models.ImageField() #falta upload_to
    def __unicode__(self):
        return self.nombre
    
class PlatoForm (ModelForm):
    class Meta:
        model=Plato

class UserProfile (models.Model):
    usuario = models.OneToOneField(User, unique=True)
    misFavoritos = models.ManyToManyRel(Plato)
    def __unicode__(self):
        return self.usuario