from django.shortcuts import render_to_response
from wedding.wedding_app.models import Blog, Page, Rsvp

def home(request):
	page = Page.objects.get(name="Home")
	return render_to_response('page.html', {'page' : page, 'active' : 'home'})

def blog(request):
	blogs = Blog.objects.all().order_by("-updated")
	return render_to_response('blog.html', {'blogs' : blogs, 'active' : 'blog'})

def about(request):
	page = Page.objects.get(name="About Us")
	return render_to_response('page.html', {'page' : page, 'active' : 'about'})

def rsvp(request):
	if request.method != 'POST':
		return render_to_response('rsvp.html', {'status' : 0, 'active' : 'rsvp'})

	first = request.POST.get('first', '')
	last = request.POST.get('last', '')
	num = request.POST.get('guests', '0')

	if first == '' or last == '' or num == 0:
		return render_to_response('rsvp.html', {'status' : -1, 'active' : 'rsvp'})
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

		return render_to_response('rsvp.html', {'first' : first, 'last' : last,
								  'guests' : num, 'status' : 1, 'active' : 'rsvp'})

def contact(request):
	return render_to_response('contact.html', {'active' : 'contact'})

def maps(request):
	return render_to_response('maps.html', {'active' : 'maps'})

def registrations(request):
	page = Page.objects.get(name="Registration Places")
	return render_to_response('page.html', {'page' : page, 'active' : 'reg'})

def pictures(request):
	return render_to_response('pictures.html', {'active' : 'pics'})
