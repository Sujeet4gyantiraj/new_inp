# Generated by Django 2.0.7 on 2022-06-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_shop_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='custom_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField(null=True)),
                ('menu', models.CharField(max_length=50, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('perent_id', models.IntegerField(null=True)),
                ('role', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
