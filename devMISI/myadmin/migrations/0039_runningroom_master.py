# Generated by Django 3.2 on 2022-07-21 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0038_station_master_stationcat_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='runningroom_master',
            fields=[
                ('rrid', models.AutoField(primary_key=True, serialize=False)),
                ('rr_name', models.CharField(max_length=50)),
                ('rr_code', models.CharField(max_length=10, unique=True)),
                ('created_by', models.CharField(max_length=50)),
                ('lastmodified_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('lastmodified_on', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.BooleanField(default=False)),
                ('stnshortcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.station_master')),
            ],
        ),
    ]