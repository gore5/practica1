from django.conf.urls import patterns, include, url
from iTeatre.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', mainpage, name='home'),

    url(r'^escriptors$', escriptorpagina, name='escriptorsllist'),
	url(r'^escriptors/(?P<idEscriptor>\d+)/$', escriptordades, name='Dades dels escriptors'),
	url(r'^escriptors/(?P<idEscriptor>\d+)/format=(?P<format>\w+)$', escriptordades, name='Dades dels escriptorsamb format'),

	url(r'^actors$', actorpagina, name='actorsllist'),
   	url(r'^actors/(?P<idActor>\d+)/$', actordades, name='Dades dels actors'),
	url(r'^actors/(?P<idActor>\d+)/format=(?P<format>\w+)$', actordades, name='Dades dels actors amb format'),

	url(r'^directors$', directorpagina, name='directorsllist'),
	url(r'^directors/(?P<idDirector>\d+)/$', directordades, name='Dades dels directors'),
	url(r'^directors/(?P<idDirector>\d+)/format=(?P<format>\w+)$', directordades, name='Dades dels directors amb format'),

	url(r'^representacions$', representaciopagina, name='representacionsllist'),
	url(r'^representacions/(?P<idRepresentacio>\d+)/$', representaciodades, name='Dades de la representacio'),
	url(r'^representacions/(?P<idRepresentacio>\d+)/format=(?P<format>\w+)/$', representaciodades, name='Dades de la representacio amb format'),

	url(r'^obresTeatre$', obra_Teatrepagina, name='obresTeatrellist'),
	url(r'^obresTeatre/(?P<idObra>\d+)/$', obra_Teatredades, name='Dades de les Obres'),
	url(r'^obresTeatre/(?P<idObra>\d+)/format=(?P<format>\w+)$', obra_Teatredades, name='Dades de les Obres amb format'),

    url(r'^login/$','django.contrib.auth.views.login'),
    #url(r'^Teatre/', include('Teatre.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
