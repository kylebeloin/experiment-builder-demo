# Generated by Django 3.1 on 2022-04-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20220418_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='valid_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
