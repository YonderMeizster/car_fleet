# Generated by Django 4.2.1 on 2023-05-30 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_vehicle_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='company',
            new_name='enterprise',
        ),
    ]
