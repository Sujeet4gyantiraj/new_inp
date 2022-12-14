# Generated by Django 2.0.7 on 2022-06-09 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_level_desig'),
    ]

    operations = [
        migrations.CreateModel(
            name='roless',
            fields=[
                ('role', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('parent', models.CharField(blank=True, max_length=50, null=True)),
                ('rly_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=20, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('delete_flag', models.BooleanField(default=False)),
                ('designation_code', models.CharField(blank=True, max_length=20, null=True)),
                ('role_code', models.CharField(blank=True, max_length=5, null=True)),
                ('shop_code', models.CharField(max_length=50, null=True)),
                ('department_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.departMast')),
            ],
        ),
    ]
