# Generated by Django 3.2 on 2022-08-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0046_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level_Desig_temp1',
            fields=[
                ('designation_code', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('effectdate', models.DateTimeField(auto_now=True, null=True)),
                ('parent_desig_code', models.CharField(max_length=15, null=True)),
                ('department_code', models.IntegerField(null=True)),
                ('rly_unit', models.IntegerField(null=True)),
                ('pc7_levelmin', models.IntegerField(blank=True, null=True)),
                ('pc7_levelmax', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=20, null=True)),
                ('desig_user', models.IntegerField(null=True)),
                ('status', models.CharField(blank=True, max_length=2, null=True)),
                ('empno', models.CharField(blank=True, max_length=50, null=True)),
                ('d_level', models.CharField(blank=True, max_length=4, null=True)),
                ('contactnumber', models.CharField(blank=True, max_length=10, null=True)),
                ('official_email_ID', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
    ]