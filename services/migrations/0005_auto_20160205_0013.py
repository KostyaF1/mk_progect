# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_service_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(default=b'/images/1_Primary_logo_on_transparent_225x75.png', upload_to=b'services'),
        ),
    ]
