# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-20 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_images', '0009_add_uploader_fields_to_uncompressed_source_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnailgroup',
            name='regular_anonymized',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thumbnailgroup',
            name='regular_crop_anonymized',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
