# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-08-04 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0003_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='', max_length=10),
        ),
    ]
