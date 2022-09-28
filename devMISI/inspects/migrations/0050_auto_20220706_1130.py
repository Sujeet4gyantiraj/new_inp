# Generated by Django 3.2 on 2022-07-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0049_event_activty_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_activty',
            name='created_by',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='event_activty',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event_activty',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event_activty',
            name='last_modified_by',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='event_activty',
            name='last_modified_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event_activty',
            name='status',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='created_by',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='events',
            name='last_modified_by',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='last_modified_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
