# Generated by Django 3.2 on 2022-08-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0079_rename_end_date_inspection_details_inspected_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insp_mail_details',
            name='send_to',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
