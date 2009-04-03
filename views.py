from django.shortcuts import render_to_response
from wedding_app.models import Blog, Page, Rsvp
from wedding_app.forms.rsvp import RsvpForm

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
        form = RsvpForm()
        return render_to_response('rsvp.html', {'form' : form, 'status' : 0,
                                  'active' : 'rsvp'})

def contact(request):
    return render_to_response('contact.html', {'active' : 'contact'})

def maps(request):
    return render_to_response('maps.html', {'active' : 'maps'})

def gifts(request):
    page = Page.objects.get(name="Registration Places")
    return render_to_response('page.html', {'page' : page, 'active' : 'gifts'})

def pictures(request):
    return render_to_response('pictures.html', {'active' : 'pics'})
