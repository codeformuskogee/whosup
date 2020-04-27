# Generated by Django 2.2.9 on 2020-04-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='queuemember',
            name='outcome_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='queuemember',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
