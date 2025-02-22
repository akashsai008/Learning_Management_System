# Generated by Django 5.1.1 on 2024-10-05 17:23

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=300)),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='backend.department')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_url', models.URLField(max_length=500, null=True)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('course_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='backend.course')),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='backend.department')),
            ],
        ),
    ]
