from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Escriptor(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()

	def __unicode__(self):
		return self.nom


class Actor(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	
	
	def __unicode__(self):
	        return self.nom


class Director(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	

	def __unicode__(self):
		return self.nom


class nom_Obra (models.Model):
	nomObra = models.CharField(max_length=40)

	def __unicode__(self):
		return self.nomObra
	

class Representacio (models.Model):
	nomObra = models.ForeignKey(nom_Obra)
	dataInici = models.DateTimeField()
	dataFi = models.DateTimeField()
	actors = models.ManyToManyField(Actor)
	director = models.ForeignKey(Director)
	

	def __unicode__(self):
		return self.nomObra


class Obra_Teatre(models.Model):
	nomObra = models.ForeignKey(nom_Obra)
	Tipus = models.CharField(max_length=40)
	escriptor = models.ForeignKey(Escriptor)
	representacions = models.ManyToManyField(Representacio)

	def __unicode__(self):
		return self.nomObra




