# Generated by Django 4.1.3 on 2022-11-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0004_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.CharField(max_length=10),
        ),
    ]