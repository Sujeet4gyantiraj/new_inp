# Generated by Django 3.2 on 2022-07-01 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0015_divisonmaster'),
        ('inspects', '0042_alter_item_details_item_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_master',
            name='department_code',
        ),
        migrations.RemoveField(
            model_name='post_master',
            name='rly_unit_code',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='aadhaar_no',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='faxNo',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='official_mobileNo',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='personal_emailID',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='personal_mobileNo',
        ),
        migrations.AlterField(
            model_name='empmast',
            name='div_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empmast_div_id', to='myadmin.railwaylocationmaster'),
        ),
        migrations.AlterField(
            model_name='empmast',
            name='rly_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empmast_rly_id', to='myadmin.railwaylocationmaster'),
        ),
        migrations.AlterField(
            model_name='hrms',
            name='div_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='div_id', to='myadmin.railwaylocationmaster'),
        ),
        migrations.AlterField(
            model_name='hrms',
            name='rly_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rly_id', to='myadmin.railwaylocationmaster'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='department_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.departmast'),
        ),
        migrations.AlterField(
            model_name='user_request',
            name='rly_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empmast_rly_id1', to='myadmin.railwaylocationmaster'),
        ),
        migrations.DeleteModel(
            name='departMast',
        ),
        migrations.DeleteModel(
            name='Post_master',
        ),
        migrations.DeleteModel(
            name='railwayLocationMaster',
        ),
    ]
