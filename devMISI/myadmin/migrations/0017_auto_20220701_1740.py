# Generated by Django 3.2 on 2022-07-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0016_auto_20220701_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level_desig',
            name='designation_code',
        ),
        migrations.AlterField(
            model_name='level_desig',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]