# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='service',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
