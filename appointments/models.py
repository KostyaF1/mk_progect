# -*- coding: utf-8 -*- 
from django.db import models
import datetime
from services.models import Service


class Appointment(models.Model):
    name = models.CharField( max_length=225, verbose_name=u'Ваше имя')
    surname = models.CharField( max_length=225, verbose_name=u'Ваша Фамилия')
    phone = models.CharField(max_length=15, verbose_name=u'Телефон')
    brand_auto = models.CharField( max_length=225, verbose_name=u'марка автомобиля')
    model_auto = models.CharField( max_length=225, verbose_name=u'модель авто')
    VIN = models.CharField( max_length=225)
    birth_of_auto = models.IntegerField(verbose_name=u'дата выпуска автомобиля')
    service = models.ManyToManyField(Service, verbose_name=u'вид сервиса')
    message = models.TextField(verbose_name=u'причина обращения')
    from_email = models.EmailField(default='example@mail.com')
    create_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default = datetime.datetime.now, verbose_name=u'желаемая дата ремонта')

    def __unicode__(self):
		return self.brand_auto
