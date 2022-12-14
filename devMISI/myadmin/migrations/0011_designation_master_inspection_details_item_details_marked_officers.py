# Generated by Django 2.0.7 on 2022-06-14 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0010_empmastnew'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation_Master',
            fields=[
                ('designation_master_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('master_name', models.CharField(max_length=40)),
                ('master_email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ],
        ),
        migrations.CreateModel(
            name='Inspection_details',
            fields=[
                ('inspection_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('inspection_officer', models.CharField(max_length=20, null=True)),
                ('inspection_title', models.CharField(max_length=20, null=True)),
                ('zone', models.CharField(max_length=10)),
                ('division', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20, null=True)),
                ('location', models.CharField(max_length=20)),
                ('inspected_on', models.DateField()),
                ('target_date', models.DateField(null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=10, null=True)),
                ('created_by', models.CharField(max_length=10, null=True)),
                ('report_path', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item_details',
            fields=[
                ('item_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_title', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('status_flag', models.IntegerField(null=True)),
                ('observation', models.CharField(max_length=50, null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=10, null=True)),
                ('created_by', models.CharField(max_length=10, null=True)),
                ('inspection_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.Inspection_details')),
            ],
        ),
        migrations.CreateModel(
            name='Marked_Officers',
            fields=[
                ('marked_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('compliance', models.CharField(max_length=10, null=True)),
                ('compliance_recieved_on', models.DateTimeField(null=True)),
                ('modified_on', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('modified_by', models.CharField(max_length=10, null=True)),
                ('created_by', models.CharField(max_length=10, null=True)),
                ('item_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.Item_details')),
                ('marked_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.Designation_Master')),
            ],
        ),
    ]
