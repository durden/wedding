from django.shortcuts import render_to_response
from wedding_app.models import Blog, Page, Rsvp
from wedding_app.forms.rsvp import RsvpForm
from django.core.mail import send_mail

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
    else:
        form = RsvpForm(request.POST)
        if form.is_valid():

            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            guests = form.cleaned_data['guests']
            email = form.cleaned_data['email']

            try:
                rsvp = Rsvp.objects.get(first_name=first, last_name=last)
            # New rsvp
            except Rsvp.DoesNotExist:
                rsvp = Rsvp(first_name=first, last_name=last, email=email,
                            guests=guests)
            else:
                rsvp.first_name = first
                rsvp.last_name = last
                rsvp.guests = guests
                rsvp.email = email

            rsvp.save()

            # Send email
            msg = "A new person has entered the following rsvp via natalieandluke.com\n" + \
                  "Name: %s %s\nE-mail: %s\nNumber of guests %d\n" % \
                  (first, last, email, guests)

            send_mail('New Wedding RSVP', msg, 'rsvp@natalieandluke.com',
                     ['durden2.0@gmail.com'], fail_silently=True)

            return render_to_response('rsvp.html', {'active' : 'rsvp',
                                      'status' : 1})
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
