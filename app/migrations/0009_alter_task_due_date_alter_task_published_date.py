# Generated by Django 5.1.2 on 2024-10-27 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_task_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 27, 17, 55, 34, 465613, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 27, 17, 55, 34, 465540, tzinfo=datetime.timezone.utc)),
        ),
    ]