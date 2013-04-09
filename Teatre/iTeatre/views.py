from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from models import *


def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Teatre aPP',
		'pagetitle': 'Benvingut a la aplicacio de Teatres',
		'contentbody': 'Aqui podras administrar coses de Teatre',
		'user': request.user
	})
	output = template.render(variables)
	return HttpResponse(output)


def escriptorpagina(request):

	escriptor = Escriptor.objects.all()
	template = get_template('llistar.html')
	variables = Context({
		'pagetitle': 'Llista de escriptors',
		'contentbody': escriptor,
	})
	output = template.render(variables)
	return HttpResponse(output)

def actorpagina(request):

	actor = Actor.objects.all()
	template = get_template('llistar.html')
	variables = Context({
		'pagetitle': 'Llista de actors',
		'contentbody': actor,
	})
	output = template.render(variables)
	return HttpResponse(output)

def directorpagina(request):

	director = Director.objects.all()
	template = get_template('llistar.html')
	variables = Context({
		'pagetitle': 'Llista de Directors',
		'contentbody': director,
	})
	output = template.render(variables)
	return HttpResponse(output)

def representaciopagina(request):

	representacio = Representacio.objects.all()
	template = get_template('llistar.html')
	variables = Context({
		'pagetitle': 'Llista de Representacions',
		'contentbody': representacio,
	})
	output = template.render(variables)
	return HttpResponse(output)

def obra_Teatrepagina(request):

	obra_Teatre = Obra_Teatre.objects.all()
	template = get_template('llistar.html')
	variables = Context({
		'pagetitle': 'Llista de obres de teatre',
		'contentbody': obra_Teatre,
	})
	output = template.render(variables)
	return HttpResponse(output)

def info_obra_Teatrepagina(request):
	
	obra_Teatre = Obra_Teatre.objects.all()
	template = get_template('infoObresTeatre.html')
	variables = Context({
		'pagetitle': 'Informacio de les obres de teatre',
		'contentbody': obra_Teatre,
	})
	output = template.render(variables)
	return HttpResponse(output)






