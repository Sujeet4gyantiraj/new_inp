# Generated by Django 3.2.13 on 2022-06-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0024_alter_marked_officers_compliance'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection_details',
            name='inspection_note_no',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
