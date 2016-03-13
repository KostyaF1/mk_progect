# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_option'),
        ('feedbacks', '0002_auto_20151229_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('surname', models.CharField(max_length=225, verbose_name='\u0412\u0430\u0448\u0430 \u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('phone', models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('brand_auto', models.CharField(max_length=225, verbose_name='\u043c\u0430\u0440\u043a\u0430 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f')),
                ('model_auto', models.CharField(max_length=225, verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e')),
                ('VIN', models.CharField(max_length=225)),
                ('birth_of_auto', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u0432\u044b\u043f\u0443\u0441\u043a\u0430 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f')),
                ('message', models.TextField(verbose_name='\u043f\u0440\u0438\u0447\u0438\u043d\u0430 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f')),
                ('from_email', models.EmailField(max_length=75)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('service', models.ManyToManyField(to='services.Service', verbose_name='\u0432\u0438\u0434 \u0441\u0435\u0440\u0432\u0438\u0441\u0430')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
