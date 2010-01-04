"""Models for wedding app"""

from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    """Editable website page"""

    name = models.CharField(max_length=20)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Rsvp(models.Model):
    """RSVP information"""

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    guests = models.PositiveSmallIntegerField()
    email = models.EmailField(blank=True)
    attending = models.BooleanField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Blog(models.Model):
    """Blog post"""

    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """Blog comment"""

    updated = models.DateField(auto_now=True)
    author = models.CharField(max_length=20)
    text = models.TextField()
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.text


class Message(models.Model):
    """Wedding message"""

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    sent = models.DateField(auto_now=True)

    def __unicode__(self):
        return u'%s (%s) ---- %s (%s)' % \
                (self.name, self.email, self.title, self.sent)
