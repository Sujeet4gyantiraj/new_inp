# Generated by Django 3.2 on 2022-07-21 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0041_inspectiontype_master_section_master_train_master_traincat_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='roster_detail',
            fields=[
                ('rostdetailid', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('roster_id', models.CharField(max_length=30)),
                ('inspection_officer_id', models.CharField(max_length=30)),
                ('doi', models.DateTimeField(auto_now=True)),
                ('inspectionof', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=30)),
                ('startstn', models.CharField(max_length=30)),
                ('endstn', models.CharField(max_length=30)),
                ('status', models.IntegerField(max_length=1, null=True)),
                ('created_by', models.CharField(blank=True, max_length=20, null=True)),
                ('lastmodified_by', models.CharField(blank=True, max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('lastmodified_on', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.BooleanField(default=False)),
                ('inspectiontype_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.inspectiontype_master')),
            ],
        ),
        migrations.CreateModel(
            name='einsp_roster',
            fields=[
                ('erosterid', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('fromdate', models.DateTimeField()),
                ('todate', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('created_by', models.CharField(blank=True, max_length=20, null=True)),
                ('lastmodified_by', models.CharField(blank=True, max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('lastmodified_on', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.BooleanField(default=False)),
                ('rly_id_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.railwaylocationmaster')),
            ],
        ),
    ]
