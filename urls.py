from django.conf.urls.defaults import *
from wedding.views import *
from django.contrib import admin
from django.conf.urls.defaults import *
from wedding.wedding_app.models import Blog

admin.autodiscover()

info = {
	'queryset' : Blog.objects.all().order_by("-updated"),
	'date_field' : 'updated',
	'make_object_list' : True,
}

urlpatterns = patterns('django.views.generic.date_based',
    # Example:
    # (r'^wedding/', include('wedding.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/(.*)', admin.site.root),
	(r'^$', home),
	(r'^blog/$', blog),
	(r'^about/$', about),
	(r'^rsvp/$', rsvp),
	(r'^contact/$', contact),
	(r'^maps/$', maps),
	(r'^registrations/$', registrations),
	(r'^pictures/$', pictures),
	(r'^blog/(?P<year>\d{4})/$','archive_year', info),
	# FIXME
	#(r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day', info),
)
