# Generated by Django 3.2 on 2022-07-06 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspects', '0050_auto_20220706_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection_details',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='inspects.empmast'),
        ),
        migrations.AlterField(
            model_name='inspection_details',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to='inspects.empmast'),
        ),
    ]
