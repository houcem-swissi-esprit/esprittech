# Generated by Django 5.0.6 on 2024-07-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdiapp', '0003_rename_domain_researchteam_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='label',
            field=models.CharField(default='project', max_length=32, unique=True),
        ),
    ]
