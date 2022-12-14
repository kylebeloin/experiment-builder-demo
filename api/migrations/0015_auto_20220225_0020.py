# Generated by Django 3.1 on 2022-02-25 00:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0014_userresponse_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('config', models.JSONField(blank=True, null=True)),
                ('options', models.JSONField(blank=True, null=True)),
                ('participants', models.ManyToManyField(blank=True, related_name='experiements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='experiements',
            field=models.ManyToManyField(blank=True, related_name='modules', to='api.Experiment'),
        ),
    ]
