from wedding.wedding_app.models import Rsvp
from django import forms

class RsvpForm(forms.ModelForm):
    class Meta:
        model = Rsvp

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    email = forms.EmailField()
