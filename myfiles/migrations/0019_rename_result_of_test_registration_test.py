# Generated by Django 4.1.3 on 2022-11-23 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0018_registration_result_of_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='result_of_test',
            new_name='test',
        ),
    ]
