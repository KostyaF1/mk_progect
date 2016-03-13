# -*- coding: utf-8 -*- 
from django.db import models
from services.models import Service

class Position(models.Model):
    name = models.CharField( max_length=225, verbose_name=u'Наименование',)
    def __unicode__(self):
        return self.name
    def get_context_data(self, **kwargs):
        context = super(Position, self).get_context_data(**kwargs)
        context['Positions'] = u"Должности"
        return context 

class Master(models.Model):
    name = models.CharField( max_length=225, verbose_name=u'имя')
    surname = models.CharField(max_length=225, verbose_name=u'фамилия')
    date_of_birth = models.DateField(verbose_name=u'дата рождения')
    email = models.EmailField()
    phone = models.CharField(max_length=15, verbose_name=u'телефон')
    address = models.CharField(max_length=225, verbose_name=u'адрес')
    skype = models.CharField(max_length=50)
    passport = models.CharField( max_length=225, verbose_name=u'паспортные данные')
    services = models.ManyToManyField(Service, verbose_name=u'выполняет сервис')
    main_position = models.ForeignKey(Position, related_name="main_position", verbose_name=u'Основная должность', blank=True, null=True)
    second_position = models.ForeignKey(Position, related_name="second_position", verbose_name=u'Второстепенная должность', blank=True, null=True)
    
    def full_name(self):
        return self.name + " " + self.surname
    def __unicode__(self):
        return self.name + " " + self.surname
