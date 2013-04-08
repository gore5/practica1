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







