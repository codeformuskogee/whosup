# Generated by Django 2.2.9 on 2020-04-14 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queue_management', '0002_auto_20200413_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuemember',
            name='outcome_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='queue_management.Outcome'),
        ),
    ]
