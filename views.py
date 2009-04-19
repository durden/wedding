from django.shortcuts import render_to_response
from wedding_app.models import Blog, Page, Rsvp
from wedding_app.forms.forms import RsvpForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def __render_page__(name, active):
    page = Page.objects.get(name=name)
    return render_to_response('page.html', {'page' : page, 'active' : active})

def home(request):
    return __render_page__("Home", "home")

def blog(request, page=1):
    blogs = Blog.objects.all().order_by("-updated")
    p = Paginator(blogs, 5)

    try:
        pages = p.page(page)
    except (EmptyPage, InvalidPage):
        pages = p.page(p.num_pages)

    return render_to_response('blog.html', {'pages' : pages, 'active' : 'blog'})

def about(request):
    return __render_page__("About Us", "about")

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

            # Build this string first b/c we can't append to a string with 
            # '+' after using the %d, %s, etc. modifiers
            # i.e this doesn't work --  x = "%s" + "a" % ('y')
            user_info = "Name: %s %s\nE-mail: %s\nAttending: %s\nNumber of guests: %d\n\n\n" % \
                        (first, last, email, request.POST['attending'], guests)

            our_msg = "A new person has entered the following rsvp via " + \
                      "natalieandluke.com\n" + user_info + \
                      "See all current rsvps: www.natalieandluke.com/attendees"

            their_msg = "Thanks for your Wedding RSVP.\nHere are the details " + \
                        "so you don't forget:\nDate: October 17, 2009 " + \
                        "\nTime:n/a\nLocation:n/a\n"

            # Send email
            try:
                send_mail('New Wedding RSVP', our_msg, 'rsvp@natalieandluke.com',
                         ['durdenmisc@gmail.com'])
                if rsvp.email != "":
                    send_mail('Luke and Natalie\'s Wedding RSVP', their_msg,
                              'rsvp@natalieandluke.com', [email, 'rsvp@natalieandluke.com'])
            # Header had \n in it, injection attempt
            except BadHeaderError:
                return render_to_response('rsvp.html', {'active' : 'rsvp',
                                          'status' : 0})

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
    return __render_page__("Registration Places", "gifts")

def pictures(request):
    return render_to_response('pictures.html', {'active' : 'pics'})

def attendees(request):
    rsvps = Rsvp.objects.all().order_by("-attending", "-last_name")
    total = 0
    for rsvp in rsvps:
        if rsvp.attending:
            total = total + rsvp.guests
    return render_to_response('attendees.html', {'active' : 'rsvp', 'rsvps' : rsvps,
                              'total' : total})
