# Generated by Django 4.1.3 on 2022-12-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0023_alter_result_time_alter_worker_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q', models.TextField()),
                ('V1', models.CharField(blank=True, max_length=50, null=True)),
                ('V2', models.CharField(blank=True, max_length=50, null=True)),
                ('V3', models.CharField(blank=True, max_length=50, null=True)),
                ('V4', models.CharField(blank=True, max_length=50, null=True)),
                ('Answer', models.CharField(blank=True, choices=[('V1', 'V1'), ('V2', 'V2'), ('V3', 'V3'), ('V4', 'V4')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=30)),
                ('tg_id', models.IntegerField()),
                ('quiz', models.IntegerField(blank=True, null=True)),
                ('answer_id', models.IntegerField(blank=True, null=True)),
                ('answer', models.CharField(blank=True, max_length=30, null=True)),
                ('result', models.CharField(blank=True, max_length=10, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='registration',
            name='test',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Result of test'),
        ),
    ]
