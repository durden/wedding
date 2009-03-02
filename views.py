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
	if request.method == 'POST':
		name = request.POST.get('name', '')
		guests = request.POST.get('guests', '0')

		#FIXME Sanitize input and make sure they aren't already in the db

		if name == '' or guests == 0:
			return render_to_response('rsvp.html', {'urls' : urls, 'submit' : 1,
									  'fail' : 1})
		else:
			return render_to_response('rsvp.html', {'urls' : urls, 'name' : name,
									  'guests' : guests, 'submit' : 1, 'fail' : 0})
	else:
		return render_to_response('rsvp.html', {'urls' : urls})

def contact(request):
	return render_to_response('contact.html', {'urls' : urls})

def maps(request):
	return render_to_response('maps.html', {'urls' : urls})

def registrations(request):
	return render_to_response('registrations.html', {'urls' : urls})

def pictures(request):
	return render_to_response('pictures.html', {'urls' : urls})
