# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-03 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0089_add_image_designated_iotd_submitters_and_reviewers'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='referral_code',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
