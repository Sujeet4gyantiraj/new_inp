# Generated by Django 3.2 on 2022-08-04 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0078_auto_20220801_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspection_details',
            old_name='end_date',
            new_name='inspected_on',
        ),
    ]