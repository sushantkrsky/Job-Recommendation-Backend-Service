# Generated by Django 5.0.6 on 2024-10-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('required_skills', models.JSONField()),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=50)),
                ('experience_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skills', models.JSONField()),
                ('experience_level', models.CharField(max_length=50)),
                ('desired_roles', models.JSONField()),
                ('locations', models.JSONField()),
                ('job_type', models.CharField(max_length=50)),
            ],
        ),
    ]
