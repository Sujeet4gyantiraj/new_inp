# Generated by Django 3.2 on 2022-07-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0068_alter_empmast_station_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
