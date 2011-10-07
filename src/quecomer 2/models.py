from django.db import models

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
    ingrediente1 = models.ForeignKey('Ingrediente', related_name='ing1')
    ingrediente2 = models.ForeignKey('Ingrediente', related_name='ing2')
    ingrediente3 = models.ForeignKey('Ingrediente', related_name='ing3')
    ingrediente4 = models.ForeignKey('Ingrediente', related_name='ing4')
    ingrediente5 = models.ForeignKey('Ingrediente', related_name='ing5')
    ingrediente6 = models.ForeignKey('Ingrediente', related_name='ing6')
    ratio_ing1 = models.IntegerField()
    ratio_ing2 = models.IntegerField()
    ratio_ing3 = models.IntegerField()
    ratio_ing4 = models.IntegerField()
    ratio_ing5 = models.IntegerField()
    ratio_ing6 = models.IntegerField()
    gramos = models.IntegerField()
    kcal = models.IntegerField()
#    foto = models.ImageField() #falta upload_to
    def __unicode__(self):
        return self.nombre
    
class UserPref(models.Model):
    misFavoritos = models.ManyToManyRel(Plato)
    def __unicode__(self):
        return self.nombre