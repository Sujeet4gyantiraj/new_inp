# Generated by Django 3.2 on 2022-08-01 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0077_auto_20220801_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspection_details',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='inspection_details',
            name='division',
        ),
        migrations.RemoveField(
            model_name='inspection_details',
            name='inspected_on',
        ),
        migrations.RemoveField(
            model_name='inspection_details',
            name='location',
        ),
        migrations.RemoveField(
            model_name='inspection_details',
            name='zone',
        ),
    ]