from django.shortcuts import render_to_response
from wedding_app.models import Blog, Page, Rsvp
from wedding_app.forms.forms import RsvpForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def home(request):
    page = Page.objects.get(name="Home")
    return render_to_response('page.html', {'page' : page, 'active' : 'home'})

def blog(request, page=1):
    blogs = Blog.objects.all().order_by("-updated")
    p = Paginator(blogs, 5)

    try:
        pages = p.page(page)
    except (EmptyPage, InvalidPage):
        pages = p.page(p.num_pages)

    return render_to_response('blog.html', {'pages' : pages, 'active' : 'blog'})

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

            attending = False
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            guests = form.cleaned_data['guests']
            email = form.cleaned_data['email']

            # Don't use cleaned_data b/c it doesn't ever evaluate to false for
            # some reason
            if request.POST['attending'] == "Yes":
                attending = True

            try:
                rsvp = Rsvp.objects.get(first_name=first, last_name=last)
            # New rsvp
            except Rsvp.DoesNotExist:
                rsvp = Rsvp(first_name=first, last_name=last, email=email,
                            guests=guests, attending=attending)
            else:
                rsvp.first_name = first
                rsvp.last_name = last
                rsvp.guests = guests
                rsvp.email = email
                rsvp.attending = attending

            rsvp.save()

            # Send email
            msg = "A new person has entered the following rsvp via natalieandluke.com\n" + \
                  "Name: %s %s\nE-mail: %s\nAttending: %s\nNumber of guests %d\n" % \
                  (first, last, email, form.cleaned_data['attending'], guests)

            #try:
                #send_mail('New Wedding RSVP', msg, 'rsvp@natalieandluke.com',
                #         ['durdenmisc@gmail.com'])
            # Header had \n in it, injection attempt
            #except BadHeaderError:
            #    return render_to_response('rsvp.html', {'active' : 'rsvp',
            #                              'status' : 0})

            return render_to_response('rsvp.html', {'active' : 'rsvp',
                                      'status' : 1, 'attending' : attending})

        return render_to_response('rsvp.html', {'form' : form, 'status' : 0,
                                  'active' : 'rsvp'})

def contact(request):
    if request.method != 'POST':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            subj = form.cleaned_data['subject']
            msg = form.cleaned_data['message']
            email = form.cleaned_data['email']

            msg = 'The following message was received from natalieandluke.com\n' +\
                  'Name: %s\nE-mail:%s\nMessage:%s\n' % (subj, email, msg)
            try:
                send_mail('New Wedding Message', msg, 'contact@natalieandluke.com',
                         ['durdenmisc@gmail.com'])
            # Header had \n in it, injection attempt
            except BadHeaderError:
                return render_to_response('contact.html', {'active' : 'contact',
                                          'form' : form, 'status' : 0})

            return render_to_response('contact.html', {'active' : 'contact',
                                      'form' : form, 'status' : 1})

    return render_to_response('contact.html', {'active' : 'contact', 'form' : form,
                              'status' : 0})

def maps(request):
    return render_to_response('maps.html', {'active' : 'maps'})

def gifts(request):
    page = Page.objects.get(name="Registration Places")
    return render_to_response('page.html', {'page' : page, 'active' : 'gifts'})

def pictures(request):
    return render_to_response('pictures.html', {'active' : 'pics'})
