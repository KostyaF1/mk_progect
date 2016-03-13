from django.db import models
from django.core.urlresolvers import reverse

class Slide(models.Model):
    name = models.CharField(max_length=225)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='sldes')
    def __unicode__(self):
		return self.name

