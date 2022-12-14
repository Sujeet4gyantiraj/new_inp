# Generated by Django 3.2.13 on 2022-06-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0010_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='empmast',
            fields=[
                ('empno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=50, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('appointmentdate', models.DateField(null=True)),
                ('sex', models.CharField(max_length=10, null=True)),
                ('marital_status', models.CharField(max_length=10, null=True)),
                ('decode_paycategory', models.CharField(max_length=50, null=True)),
                ('billunit', models.CharField(max_length=50, null=True)),
                ('service_status', models.CharField(max_length=50, null=True)),
                ('emp_status', models.CharField(max_length=50, null=True)),
                ('rectt_category', models.CharField(max_length=50, null=True)),
                ('payband', models.CharField(max_length=10, null=True)),
                ('scalecode', models.CharField(max_length=50, null=True)),
                ('pc7_level', models.CharField(max_length=10, null=True)),
                ('payrate', models.CharField(max_length=50, null=True)),
                ('office', models.CharField(max_length=50, null=True)),
                ('office_orderno', models.CharField(max_length=100, null=True)),
                ('station_des', models.CharField(max_length=50, null=True)),
                ('emptype', models.CharField(max_length=10, null=True)),
                ('medicalcode', models.CharField(max_length=50, null=True)),
                ('tradecode', models.CharField(max_length=50, null=True)),
                ('dept_desc', models.CharField(max_length=50, null=True)),
                ('parentshop', models.CharField(max_length=50, null=True)),
                ('shopno', models.CharField(max_length=50, null=True)),
                ('desig_longdesc', models.CharField(max_length=50, null=True)),
                ('wau', models.CharField(max_length=50, null=True)),
                ('inc_category', models.CharField(max_length=50, null=True)),
                ('emp_inctype', models.CharField(max_length=50, null=True)),
                ('parent', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('contactno', models.CharField(blank=True, max_length=10, null=True)),
                ('ticket_no', models.CharField(blank=True, max_length=12, null=True)),
                ('idcard_no', models.CharField(blank=True, max_length=15, null=True)),
                ('op_read', models.BooleanField(default=True)),
                ('op_create', models.BooleanField(default=False)),
                ('op_delete', models.BooleanField(default=False)),
                ('op_update', models.BooleanField(default=False)),
                ('shop_section', models.CharField(max_length=9, null=True)),
                ('profile_modified_by', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_modified_on', models.DateField(blank=True, null=True)),
                ('date_of_promotion', models.DateField(null=True)),
                ('date_of_joining', models.DateField(null=True)),
            ],
        ),
    ]
