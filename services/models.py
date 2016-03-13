from django.conf import settings
from django.conf.urls.static import static
from django.db import models
from django.core.urlresolvers import reverse

class Service(models.Model):
    name = models.CharField(max_length=225)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='services',
                              default = "/images/1_Primary_logo_on_transparent_225x75.png")
    def __unicode__(self):
		return self.name

class Option(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    service = models.ForeignKey(Service)
    order = models.PositiveIntegerField()
	
    def __unicode__(self):
        return self.name
'''
    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'pk': self.course.id})
'''
