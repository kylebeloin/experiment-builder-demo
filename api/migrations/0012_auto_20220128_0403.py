# Generated by Django 3.1 on 2022-01-28 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s3', '0002_auto_20220128_0359'),
        ('api', '0011_question_config'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='UserResponse',
        ),
    ]
