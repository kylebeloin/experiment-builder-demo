# Generated by Django 2.2.13 on 2022-01-15 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_completedmodule_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complete',
            new_name='completed',
        ),
        migrations.AddField(
            model_name='completedmodule',
            name='result',
            field=models.FloatField(default=0),
        ),
    ]
