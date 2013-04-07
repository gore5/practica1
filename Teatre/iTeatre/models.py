from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Actor(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	
	

class Obra_Teatre(models.Model):
	nomObra = models.CharField(max_length=40)
	Tipus = models.CharField(max_length=40)
	date = models.DateTimeField()
	

class Escriptor(models.Model):
	nom = models.CharField(max_length=40)
	obra = models.ForeignKey(Obra_Teatre)

class Director(models.Model):
	nom = models.CharField(max_length=40)
	obra = models.ForeignKey(Obra_Teatre)

Actor.add_to_class('obra', models.ForeignKey(Obra_Teatre))
Obra_Teatre.add_to_class('actor', models.ForeignKey(Actor))
Obra_Teatre.add_to_class('director', models.ForeignKey(Director))
Obra_Teatre.add_to_class('escriptor', models.ForeignKey(Escriptor))
'''Escriptor.add_to_class('obra', models.ForeignKey(Obra_Teatre))
Director.add_to_class('obra', models.ForeignKey(Obra_Teatre))'''
