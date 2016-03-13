# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_remove_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0436\u0435\u043b\u0430\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u0440\u0435\u043c\u043e\u043d\u0442\u0430'),
            preserve_default=True,
        ),
    ]
