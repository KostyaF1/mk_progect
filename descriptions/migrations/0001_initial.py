# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=225)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', models.ImageField(default=b'/images/1_Primary_logo_on_transparent_225x75.png', upload_to=b'descriptions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppointmentOnline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=225)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', models.ImageField(default=b'/images/1_Primary_logo_on_transparent_225x75.png', upload_to=b'descriptions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
