from django.conf.urls.defaults import *
from wedding.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wedding/', include('wedding.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
	(r'^$', home),
	(r'^blog/$', blog),
	(r'^about/$', about),
	(r'^rsvp/$', rsvp),
	(r'^contact/$', contact),
	(r'^maps/$', maps),
	(r'^registrations/$', registrations),
	(r'^pictures/$', pictures),
)
