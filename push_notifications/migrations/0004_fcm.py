# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
		('push_notifications', '0003_wnsdevice'),
	]

	operations = [
		migrations.AddField(
			model_name='gcmdevice',
			name='cloud_message_type',
			field=models.CharField(choices=[('FCM', 'Firebase Cloud Message'), ('GCM', 'Google Cloud Message')], default='GCM', help_text='You should choose GCM or FCM', max_length=3, verbose_name='Cloud Message Type')
		),
	]
