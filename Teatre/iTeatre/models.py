from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Escriptor(models.Model):
	nom = models.CharField(max_length=40)

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
	

	def __unicode__(self):
		return self.nom

class Obra_Teatre(models.Model):
	nomObra = models.CharField(max_length=40)
	Tipus = models.CharField(max_length=40)
	date = models.DateTimeField()
	actors = models.ManyToManyField(Actor)
	escriptor = models.ForeignKey(Escriptor)
	director = models.ForeignKey(Director)

	def __unicode__(self):
		return self.nomObra



