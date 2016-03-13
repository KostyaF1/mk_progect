# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0006_auto_20151224_2356'),
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='main_position',
            field=models.ForeignKey(related_name=b'main_manager', verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', blank=True, to='masters.Position', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manager',
            name='second_position',
            field=models.ForeignKey(related_name=b'second_manager', verbose_name='\u0412\u0442\u043e\u0440\u043e\u0441\u0442\u0435\u043f\u0435\u043d\u043d\u0430\u044f \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', blank=True, to='masters.Position', null=True),
            preserve_default=True,
        ),
    ]
