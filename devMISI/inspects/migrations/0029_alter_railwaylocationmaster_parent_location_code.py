# Generated by Django 3.2 on 2022-06-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0028_auto_20220622_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='railwaylocationmaster',
            name='parent_location_code',
            field=models.CharField(max_length=10),
        ),
    ]
