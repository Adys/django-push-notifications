# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0007_gcmdevice_migrate_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gcmdevice',
            name='device_id',
        ),
        migrations.RenameField(
            model_name='gcmdevice',
            old_name='device_uuid',
            new_name='device_id',
        ),
    ]
