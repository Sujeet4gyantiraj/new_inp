# Generated by Django 2.0.7 on 2022-06-14 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0021_auto_20220614_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='marked_officers_forward',
            name='myuser_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='marked_officers_forward',
            name='compliance_forward',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
