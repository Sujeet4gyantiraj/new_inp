# Generated by Django 3.2 on 2022-08-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0085_alter_item_details_item_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_details',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
