# Generated by Django 4.1.3 on 2022-11-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0007_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Answer',
            field=models.BooleanField(blank=True, choices=[(models.CharField(blank=True, max_length=50, null=True), 'V1'), (models.CharField(blank=True, max_length=50, null=True), 'V2'), (models.CharField(blank=True, max_length=50, null=True), 'V3'), (models.CharField(blank=True, max_length=50, null=True), 'V4')], null=True),
        ),
    ]
