# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0005_auto_20151224_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='address',
            field=models.CharField(max_length=225, verbose_name='\u0430\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='master',
            name='date_of_birth',
            field=models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=225, verbose_name='\u0438\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='master',
            name='passport',
            field=models.CharField(max_length=225, verbose_name='\u043f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435'),
        ),
        migrations.AlterField(
            model_name='master',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='master',
            name='services',
            field=models.ManyToManyField(to=b'services.Service', verbose_name='\u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0435\u0442 \u0441\u0435\u0440\u0432\u0438\u0441'),
        ),
        migrations.AlterField(
            model_name='master',
            name='surname',
            field=models.CharField(max_length=225, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=225, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
