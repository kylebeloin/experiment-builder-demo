# Generated by Django 3.1 on 2022-02-25 06:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0016_auto_20220225_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='experiements',
            new_name='experiments',
        ),
        migrations.AddField(
            model_name='experiment',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='experiments', to=settings.AUTH_USER_MODEL),
        ),
    ]
