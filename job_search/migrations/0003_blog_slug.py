# Generated by Django 4.2.3 on 2023-07-20 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
