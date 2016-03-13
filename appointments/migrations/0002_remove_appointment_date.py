# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
    ]
