# Generated by Django 3.2 on 2022-07-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0033_alter_railwaylocationmaster_location_type_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empmastnew',
            name='emp_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
