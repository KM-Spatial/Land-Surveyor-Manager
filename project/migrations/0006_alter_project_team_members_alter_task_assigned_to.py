# Generated by Django 4.0.2 on 2022-05-23 12:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0005_alter_project_team_members_alter_task_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team_members',
            field=models.ManyToManyField(blank=True, related_name='team_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
