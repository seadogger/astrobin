# Generated by Django 2.2.24 on 2024-05-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0148_equipmentitemmarketplacelistinglineitem_mark_as_sold_reminder_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentitemmarketplacelistinglineitem',
            name='rate_buyer_reminder_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
