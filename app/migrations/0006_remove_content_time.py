# Generated by Django 5.1.2 on 2024-10-26 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_content_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='time',
        ),
    ]