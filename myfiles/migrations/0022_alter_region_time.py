# Generated by Django 4.1.3 on 2022-11-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0021_region_registration_region_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
