# Generated by Django 3.2 on 2022-08-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0043_level_desig_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='level_desig',
            name='contactnumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='level_desig',
            name='official_email_ID',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
