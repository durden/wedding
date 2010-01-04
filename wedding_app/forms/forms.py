"""Forms for wedding app"""

from wedding.wedding_app.models import Rsvp
from django import forms


class RsvpForm(forms.ModelForm):
    """RSVP form"""

    choices = (('Yes', 'Yes'), ('No', 'No'))
    attending = forms.BooleanField(widget=forms.RadioSelect(choices=choices))
    class Meta:
        """Tie RSVP model to this form"""
        model = Rsvp


class ContactForm(forms.Form):
    """Contact form"""

    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 10,
                                                           'cols': 60}))
    email = forms.EmailField()
