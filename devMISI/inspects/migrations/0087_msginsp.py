# Generated by Django 3.2.10 on 2022-09-12 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0047_level_desig_temp1'),
        ('inspects', '0086_item_details_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='MsgInsp',
            fields=[
                ('msg_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('msg_sent', models.CharField(max_length=500, null=True)),
                ('msg_reply', models.CharField(max_length=500, null=True)),
                ('msg_by', models.CharField(max_length=15, null=True)),
                ('msg_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.level_desig')),
            ],
        ),
    ]
