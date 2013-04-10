from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from models import *



def mainpage(request):

	template = get_template('index.html')
	variables = Context({
		'titlehead': 'Teatre aPP',
		'pagetitle': 'Benvingut a la aplicacio de Teatres',
		'contentbody': 'Aqui podras administrar coses de Teatre',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


#--------------------------------------------ESCRIPTOR------------------------------------------------

def escriptorpagina(request):

	escriptor = Escriptor.objects.all()
	template = get_template('llista.html')
	variables = Context({
		'pagetitle': 'Llista de escriptors',
		'contentbody': escriptor,
		'name':'/escriptors/',
	})
	output = template.render(variables)
	return HttpResponse(output)

def escriptordades(request, idEscriptor):

	escriptor = Escriptor.objects.get(id=idEscriptor)
	template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del escriptor',
		'contentbody': escriptor,
	})
	output = template.render(variables)
	return HttpResponse(output)


#----------------------------------------------ACTOR--------------------------------------------------

def actorpagina(request):

	actor = Actor.objects.all()
	template = get_template('llista.html')
	variables = Context({
		'pagetitle': 'Llista de actors',
		'contentbody': actor,
		'name':'/actors/',
	})
	output = template.render(variables)
	return HttpResponse(output)

def actordades(request, idActor):

	actor = Actor.objects.get(id=idActor)
	template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del actor',
		'contentbody': actor,
	})
	output = template.render(variables)
	return HttpResponse(output)


#--------------------------------------------DIRECTOR------------------------------------------------

def directorpagina(request):

	director = Director.objects.all()
	template = get_template('llista.html')
	variables = Context({
		'pagetitle': 'Llista de Directors',
		'contentbody': director,
		'name':'/directors/',
	})
	output = template.render(variables)
	return HttpResponse(output)

def directordades(request, idDirector):

	director = Director.objects.get(id=idDirector)
	template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del director',
		'contentbody': director,
	})
	output = template.render(variables)
	return HttpResponse(output)


#--------------------------------------------REPRESENTACIO------------------------------------------------

def representaciopagina(request):

	representacio = Representacio.objects.all()
	template = get_template('llistar.html')
	variables = Context({
		'pagetitle': 'Llista de Representacions',
		'contentbody': representacio,
	})
	output = template.render(variables)
	return HttpResponse(output)


#-------------------------------------------------OBRA-----------------------------------------------------

def obra_Teatrepagina(request):

	obra_Teatre = Obra_Teatre.objects.all()
	template = get_template('llista.html')
	variables = Context({
		'pagetitle': 'Llista de obres de teatre',
		'contentbody': obra_Teatre,
		'name':'/obresTeatre/',
	})
	output = template.render(variables)
	return HttpResponse(output)


def obra_Teatredades(request, idObra):

	obra_Teatre  = Obra_Teatre.objects.get(id=idObra)
	template = get_template('infoObresTeatre.html')
	variables = Context({
		'pagetitle': 'Informacio de les obres de teatre',
		'contentbody': obra_Teatre,
	})
	output = template.render(variables)
	return HttpResponse(output)







