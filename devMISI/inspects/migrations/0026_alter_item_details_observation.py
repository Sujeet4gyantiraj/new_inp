# Generated by Django 3.2.13 on 2022-06-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0025_inspection_details_inspection_note_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_details',
            name='observation',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
