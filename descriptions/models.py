from django.db import models

class AboutUs(models.Model):
    name = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='descriptions',
                              default = "/images/1_Primary_logo_on_transparent_225x75.png")
    def __unicode__(self):
		return self.name

class AppointmentOnline(models.Model):
    name = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='descriptions',
                              default = "/images/1_Primary_logo_on_transparent_225x75.png")
    def __unicode__(self):
		return self.name
