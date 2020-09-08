# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-08 20:19
from __future__ import unicode_literals

import astrobin_apps_platesolving.models
import common.validators.file_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_platesolving', '0014_platesolvingadvancedsettings_show_cgpn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platesolvingadvancedsettings',
            name='sample_raw_frame_file',
            field=models.FileField(blank=True, help_text='To improve the accuracy of your plate-solution even further, please upload one of the XISF or FITS files from your data set. Such files normally have date and time headers that will allow AstroBin to calculate solar system body ephemerides and find planets and asteroids in your image (provided you also add location information to it).<br/><br/>For maximum accuracy, it\'s recommended that you use PixInsight\'s native and open format XISF. Learn more about XISF here:<br/><br/><a href="https://pixinsight.com/xisf/" target="_blank">https://pixinsight.com/xisf/</a><br/><br/> <strong>Please note:</strong> it\'s very important that the XISF or FITS file you upload is aligned to your processed image, otherwise the object annotations will not match. To improve your chances at a successful accurate plate-solution, calibrate your file the usual way (dark/bias/flats) but do not stretch it.', max_length=256, null=True, upload_to=astrobin_apps_platesolving.models.sample_frame_upload_path, validators=[common.validators.file_validator.FileValidator(allowed_extensions=(b'xisf', b'fits', b'fit', b'fts'))], verbose_name='Sample raw frame (max 100 MB)'),
        ),
    ]
