# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='photo',
            field=models.ImageField(default=b'/images/1_Primary_logo_on_transparent_225x75.png', height_field=b'photo_height', width_field=b'photo_width', upload_to=b'services'),
            preserve_default=True,
        ),
    ]
