# Generated by Django 3.2.13 on 2022-06-10 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0016_hrms'),
    ]

    operations = [
        migrations.AddField(
            model_name='empmast',
            name='myuser_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
