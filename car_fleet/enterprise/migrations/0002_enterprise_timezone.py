# Generated by Django 4.2.1 on 2023-06-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='timezone',
            field=models.TextField(choices=[('Etc/GMT+12', 'GMT+12'), ('Etc/GMT+11', 'GMT+11'), ('Etc/GMT+10', 'GMT+10'), ('Etc/GMT+9', 'GMT+9'), ('Etc/GMT+8', 'GMT+8'), ('Etc/GMT+7', 'GMT+7'), ('Etc/GMT+6', 'GMT+6'), ('Etc/GMT+5', 'GMT+5'), ('Etc/GMT+4', 'GMT+4'), ('Etc/GMT+3', 'GMT+3'), ('Etc/GMT+2', 'GMT+2'), ('Etc/GMT+1', 'GMT+1'), ('Etc/GMT+0', 'GMT+0'), ('Etc/GMT-0', 'GMT-0'), ('Etc/GMT-1', 'GMT-1'), ('Etc/GMT-2', 'GMT-2'), ('Etc/GMT-3', 'GMT-3'), ('Etc/GMT-4', 'GMT-4'), ('Etc/GMT-5', 'GMT-5'), ('Etc/GMT-6', 'GMT-6'), ('Etc/GMT-7', 'GMT-7'), ('Etc/GMT-8', 'GMT-8'), ('Etc/GMT-9', 'GMT-9'), ('Etc/GMT-10', 'GMT-10'), ('Etc/GMT-11', 'GMT-11'), ('Etc/GMT-12', 'GMT-12'), ('Etc/GMT-13', 'GMT-13'), ('Etc/GMT-14', 'GMT-14')], default='GMT-0'),
        ),
    ]
