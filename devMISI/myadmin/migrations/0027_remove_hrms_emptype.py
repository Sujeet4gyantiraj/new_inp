# Generated by Django 3.2 on 2022-07-14 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0026_hrms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hrms',
            name='emptype',
        ),
    ]
