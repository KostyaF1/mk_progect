# -*- coding: utf-8 -*- 
from django.db import models
import datetime
from services.models import Service


class Feedback(models.Model):
    name = models.CharField( max_length=225, verbose_name=u'Ваше имя')
    subject = models.CharField(max_length=255, verbose_name=u'тема')
    message = models.TextField(verbose_name=u'сообщение')
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
		return self.subject

