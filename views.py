from django.shortcuts import render_to_response

from wedding.settings import MEDIA_URL

urls = {
	'home' : '/', 
	'blog' : '/blog',
	'about' : '/about',
	'rsvp' : '/rsvp',
	'contact' : '/contact',
	'maps' : '/maps',
	'registrations' : '/registrations',
	'pictures' : '/pictures',
}

def home(request):
	return render_to_response('home.html', {'urls' : urls})

def blog(request):
	return render_to_response('blog.html', {'urls' : urls})

def about(request):
	return render_to_response('about.html', {'urls' : urls})

def rsvp(request):
	return render_to_response('rsvp.html', {'urls' : urls})

def contact(request):
	return render_to_response('contact.html', {'urls' : urls})

def maps(request):
	return render_to_response('maps.html', {'urls' : urls})

def registrations(request):
	return render_to_response('registrations.html', {'urls' : urls})

def pictures(request):
	return render_to_response('pictures.html', {'urls' : urls})
