# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
from masters.models import Position

class  Manager(models.Model):
    user = models.OneToOneField(User, verbose_name=u'пользователь')
    date_of_birth = models.DateField(verbose_name=u'дата рождения')
    gender = models.CharField(max_length=225, choices=(("M", "Male"),("F", "Female")), verbose_name=u'пол')
    phone = models.CharField(max_length=15, verbose_name=u'телефон')
    address = models.CharField(max_length=225, verbose_name=u'адрес')
    skype = models.CharField(max_length=50)
    passport = models.CharField( max_length=225, verbose_name=u'паспортные данные',)
    description = models.TextField(verbose_name=u'информация')
    main_position = models.ForeignKey(Position, related_name="main_manager", verbose_name=u'Основная должность', blank=True, null=True)
    second_position = models.ForeignKey(Position, related_name="second_manager", verbose_name=u'Второстепенная должность', blank=True, null=True)
    
    def __unicode__(self):
        return self.user.username
    
    def get_full_name(self):
		return self.user.first_name + " " + self.user.last_name
