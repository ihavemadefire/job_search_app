# Generated by Django 4.2.3 on 2023-07-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
    ]