# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-30 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changeset', '0042_auto_20170330_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspicionreasons',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
