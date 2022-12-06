# Generated by Django 4.1.3 on 2022-11-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0014_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Answer',
            field=models.CharField(blank=True, choices=[('V1', 'V1'), ('V2', 'V2'), ('V3', 'V3'), ('V4', 'V4')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='V1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]