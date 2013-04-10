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

def escriptordades(request, idEscriptor, format='html'):

	escriptor = Escriptor.objects.get(id=idEscriptor)
	if(format=='xml'):
		template = get_template('dades.xml')
	else:
		template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del escriptor',
		'contentbody': escriptor,
		'tag1':'escriptors',
		'tag2':'escriptor'
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

def actordades(request, idActor, format='html'):

	actor = Actor.objects.get(id=idActor)
	if(format=='xml'):
		template = get_template('dades.xml')
	else:
		template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del actor',
		'contentbody': actor,
		'tag1':'actors',
		'tag2':'actor'
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

def directordades(request, idDirector, format='html'):

	director = Director.objects.get(id=idDirector)
	if(format=='xml'):
		template = get_template('dades.xml')
	else:
		template = get_template('dades.html')
	variables = Context({
		'pagetitle': 'Dades del director',
		'contentbody': director,
		'tag1':'director',
		'tag2':'directors'
	})
	output = template.render(variables)
	return HttpResponse(output)


#--------------------------------------------REPRESENTACIO------------------------------------------------

def representaciopagina(request):

	representacio = Representacio.objects.all()
	template = get_template('llista.html')
	variables = Context({
		'pagetitle': 'Llista de Representacions',
		'contentbody': representacio,
		'name':'/representacions/',
	})
	output = template.render(variables)
	return HttpResponse(output)


def representaciodades(request, idRepresentacio, format='html'):

	representacio = Representacio.objects.get(id=idRepresentacio)
	if(format=='xml'):
		template = get_template('representacio.xml')
	else:
		template = get_template('representacio.html')
	variables = Context({
		'pagetitle': 'Informacio de la representacio',
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


def obra_Teatredades(request, idObra, format='html'):

	obra_Teatre  = Obra_Teatre.objects.get(id=idObra)
	if(format=='xml'):
		template = get_template('Obrateatre.xml')
	else:
		template = get_template('infoObresTeatre.html')
	variables = Context({
		'pagetitle': 'Informacio de les obres de teatre',
		'contentbody': obra_Teatre,
	})
	output = template.render(variables)
	return HttpResponse(output)







