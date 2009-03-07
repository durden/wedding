from django.shortcuts import render_to_response
from wedding.wedding_app.models import Blog, Page, Rsvp

urls = {
	'home' 			: '/',
	'blog' 			: '/blog',
	'about' 		: '/about',
	'rsvp' 			: '/rsvp',
	'contact' 		: '/contact',
	'maps' 			: '/maps',
	'registrations' : '/registrations',
	'pictures' 		: '/pictures',
}

def home(request):
	page = Page.objects.get(name="Home")
	return render_to_response('page.html', {'urls' : urls, 'page' : page})

def blog(request):
	blogs = Blog.objects.all().order_by("-updated")
	return render_to_response('blog.html', {'urls' : urls, 'blogs' : blogs})

def about(request):
	page = Page.objects.get(name="About Us")
	return render_to_response('page.html', {'urls' : urls, 'page' : page})

def rsvp(request):
	if request.method != 'POST':
		return render_to_response('rsvp.html', {'urls' : urls, 'status' : 0})

	first = request.POST.get('first', '')
	last = request.POST.get('last', '')
	num = request.POST.get('guests', '0')

	if first == '' or last == '' or num == 0:
		return render_to_response('rsvp.html', {'urls' : urls, 'status' : -1})
	else:
		try:
			rsvp = Rsvp.objects.get(first_name=first, last_name=last)
		except Rsvp.DoesNotExist:
			# Insert
			rsvp = Rsvp(first_name=first, last_name=last, guests=num)
		else:
			# Update
			rsvp.guests = num

		rsvp.save()

		return render_to_response('rsvp.html', {'urls' : urls, 'first' : first,
						  'last' : last, 'guests' : num, 'status' : 1})

def contact(request):
	return render_to_response('contact.html', {'urls' : urls})

def maps(request):
	return render_to_response('maps.html', {'urls' : urls})

def registrations(request):
	page = Page.objects.get(name="Registration Places")
	return render_to_response('page.html', {'urls' : urls, 'page' : page})

def pictures(request):
	return render_to_response('pictures.html', {'urls' : urls})
