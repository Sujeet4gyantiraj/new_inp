# Generated by Django 3.2 on 2022-07-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0021_adminmaster_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='level_desig',
            name='modified_by',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='level_desig',
            name='effectdate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
