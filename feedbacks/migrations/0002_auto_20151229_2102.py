# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=225, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='\u0442\u0435\u043c\u0430'),
        ),
    ]
