# Generated by Django 4.0.2 on 2022-05-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='reminder_mode',
            field=models.CharField(choices=[('email', 'email')], default='email', max_length=20),
        ),
    ]
