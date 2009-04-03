from wedding.wedding_app.models import Rsvp
from django.forms import ModelForm

class RsvpForm(ModelForm):
    class Meta:
        model = Rsvp
