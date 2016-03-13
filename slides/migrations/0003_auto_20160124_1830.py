# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20160124_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='photo',
            field=models.ImageField(upload_to=b'sldes'),
        ),
    ]
