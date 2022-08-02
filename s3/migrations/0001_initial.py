# Generated by Django 3.1 on 2022-01-28 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_question_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('filepath', models.URLField(null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('modules', models.ManyToManyField(blank=True, null=True, related_name='files', to='api.Module')),
                ('options', models.ManyToManyField(blank=True, null=True, related_name='files', to='api.Option')),
                ('questions', models.ManyToManyField(blank=True, null=True, related_name='files', to='api.Question')),
                ('response', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.response')),
            ],
        ),
    ]
