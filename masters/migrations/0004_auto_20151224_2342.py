# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0003_auto_20151224_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='position',
        ),
        migrations.AddField(
            model_name='master',
            name='main_position',
            field=models.ForeignKey(related_name=b'main_position', blank=True, to='masters.Position', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='master',
            name='second_position',
            field=models.ForeignKey(related_name=b'second_position', blank=True, to='masters.Position', null=True),
            preserve_default=True,
        ),
    ]
