# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('gender', models.CharField(max_length=225, verbose_name='\u043f\u043e\u043b', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone', models.CharField(max_length=15, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('address', models.CharField(max_length=225, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('skype', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=225, verbose_name='\u043f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435')),
                ('description', models.TextField(verbose_name='\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f')),
                ('user', models.OneToOneField(verbose_name='\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
