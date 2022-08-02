# Generated by Django 3.1 on 2022-01-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_question_config'),
        ('s3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='modules',
            field=models.ManyToManyField(blank=True, related_name='files', to='api.Module'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='options',
            field=models.ManyToManyField(blank=True, related_name='files', to='api.Option'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='files', to='api.Question'),
        ),
    ]
