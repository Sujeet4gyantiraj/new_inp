# Generated by Django 3.2 on 2022-07-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0032_hrms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='railwaylocationmaster',
            name='location_type_desc',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
