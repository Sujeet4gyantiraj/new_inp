# Generated by Django 3.2 on 2022-07-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0056_inspection_details_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='marked_officers',
            name='revert',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='marked_officers',
            name='reverted_on',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='marked_officers',
            name='status',
            field=models.CharField(max_length=1, null=True),
        ),
    ]