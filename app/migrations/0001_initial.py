# Generated by Django 5.1.2 on 2024-10-24 18:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('published_date', models.DateField(verbose_name=datetime.datetime(2024, 10, 24, 18, 18, 43, 175660, tzinfo=datetime.timezone.utc))),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('time', models.TimeField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.task')),
            ],
        ),
    ]
