# Generated by Django 3.2 on 2022-07-05 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0021_adminmaster_created_on'),
        ('inspects', '0046_alter_myuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='marked_officers',
            name='marked_emp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspects.empmast'),
        ),
        migrations.AlterField(
            model_name='inspection_details',
            name='inspection_officer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.level_desig'),
        ),
        migrations.AlterField(
            model_name='marked_officers',
            name='marked_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.level_desig'),
        ),
        migrations.AlterField(
            model_name='marked_officers_forward',
            name='marked_to_forward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.level_desig'),
        ),
        migrations.DeleteModel(
            name='Designation_Master',
        ),
    ]
