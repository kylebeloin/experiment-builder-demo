# Generated by Django 3.1 on 2022-01-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220124_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='config',
            field=models.JSONField(blank=True, null=True),
        ),
    ]