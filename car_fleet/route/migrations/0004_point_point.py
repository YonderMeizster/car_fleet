# Generated by Django 4.2.1 on 2023-07-04 07:20

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_route_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(default=None, srid=4326),
            preserve_default=False,
        ),
    ]
