# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_service_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField()),
                ('service', models.ForeignKey(to='services.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
