# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20171024_0441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vm',
            old_name='power_state',
            new_name='powerstate',
        ),
        migrations.RenameField(
            model_name='vm',
            old_name='cpu',
            new_name='vcpu',
        ),
    ]