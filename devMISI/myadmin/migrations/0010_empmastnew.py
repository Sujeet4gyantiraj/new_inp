# Generated by Django 2.0.7 on 2022-06-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0009_custom_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='empmastnew',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('shop_section', models.CharField(max_length=50, null=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.empmast')),
            ],
        ),
    ]