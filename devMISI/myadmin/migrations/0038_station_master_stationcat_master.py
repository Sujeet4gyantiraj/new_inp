# Generated by Django 3.2 on 2022-07-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0037_auto_20220721_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='station_master',
            fields=[
                ('stnshortcode', models.CharField(editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('rly_id_id', models.CharField(max_length=50)),
                ('lastmodified_by', models.CharField(max_length=50)),
                ('created_by', models.CharField(max_length=50)),
                ('station_name', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('lastmodified_on', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='stationcat_master',
            fields=[
                ('stnid', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('stn_category', models.CharField(max_length=50)),
                ('lastmodified_by', models.CharField(max_length=50)),
                ('created_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('lastmodified_on', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.BooleanField(default=False)),
            ],
        ),
    ]
