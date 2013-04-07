from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Actor(models.Model):
	nom = models.CharField(max_length=40)
	edat = models.IntegerField()
	sexe = models.CharField(max_length=1)
	
	def __unicode__(self):
	        return self.nom

	

class Obra_Teatre(models.Model):
	nomObra = models.CharField(max_length=40)
	Tipus = models.CharField(max_length=40)
	date = models.DateTimeField()
	actor = models.ForeignKey(Actor)

	def __unicode__(self):
		return self.nomObra

	

class Escriptor(models.Model):
	nom = models.CharField(max_length=40)
	obra = models.ForeignKey(Obra_Teatre)


class Director(models.Model):
	nom = models.CharField(max_length=40)
	obra = models.ForeignKey(Obra_Teatre)



class Relacio(models.Model):
	director = models.ForeignKey(Director)
	escriptor = models.ForeignKey(Escriptor)
	obra = models.ForeignKey(Obra_Teatre)
	actor = models.ForeignKey(Actor)


