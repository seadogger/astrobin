# Generated by Django 2.2.24 on 2024-01-28 21:30
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0128_add_thumbnail_to_markeplace_image'),
    ]

    operations = [
        CreateExtension('cube'),
        CreateExtension('earthdistance'),
    ]
