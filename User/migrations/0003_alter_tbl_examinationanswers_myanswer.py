# Generated by Django 5.1.6 on 2025-03-09 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cordinator', '0015_alter_tbl_examination_start_time'),
        ('User', '0002_tbl_timmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_examinationanswers',
            name='myanswer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myanswer', to='Cordinator.tbl_options'),
        ),
    ]
