# Generated by Django 3.1 on 2022-04-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_userresponse_response_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='module',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
