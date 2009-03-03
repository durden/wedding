from django.db import models

class Page(models.Model):
	name = models.CharField(max_length=20)
	text = models.TextField()
	updated = models.DateField(auto_now=True)

class Rsvp(models.Model):
	name = models.CharField(max_length=30)
	guests = models.PositiveSmallIntegerField()
	email = models.EmailField()

class Blog(models.Model):
	updated = models.DateField(auto_now=True)
	updated_by = models.CharField(max_length=20)
	text = models.TextField()

class Comment(models.Model):
	updated = models.DateField(auto_now=True)
	updated_by = models.CharField(max_length=20)
	text = models.TextField()
	blog = models.ForeignKey(Blog)	
