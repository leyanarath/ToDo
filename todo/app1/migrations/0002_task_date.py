# Generated by Django 4.2.6 on 2023-12-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2002-05-01'),
            preserve_default=False,
        ),
    ]
