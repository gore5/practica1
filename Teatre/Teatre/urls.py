from django.conf.urls import patterns, include, url
from iTeatre.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    url(r'^escriptors$', escriptorpagina, name='escriptorsllist'),
	url(r'^actors$', actorpagina, name='actorsllist'),
	url(r'^directors$', directorpagina, name='directorsllist'),
	url(r'^representacions$', representaciopagina, name='representacionsllist'),
	url(r'^obresTeatre$', obra_Teatrepagina, name='obresTeatrellist'),
	url(r'^infoObresTeatre$', info_obra_Teatrepagina, name='infoObresTeatre'),
   
    #url(r'^Teatre/', include('Teatre.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
