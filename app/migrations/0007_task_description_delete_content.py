# Generated by Django 5.1.2 on 2024-10-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_content_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='Description not provided'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='content',
        ),
    ]