# Generated by Django 3.2 on 2022-07-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0045_alter_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
