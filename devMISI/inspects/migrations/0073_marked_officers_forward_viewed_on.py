# Generated by Django 3.2 on 2022-07-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0072_auto_20220729_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='marked_officers_forward',
            name='viewed_on',
            field=models.DateField(null=True),
        ),
    ]
