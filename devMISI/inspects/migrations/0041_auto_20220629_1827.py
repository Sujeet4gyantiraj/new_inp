# Generated by Django 3.2 on 2022-06-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0040_item_details_des_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection_activity',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inspection_checklist',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
    ]
