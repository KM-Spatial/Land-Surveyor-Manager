# Generated by Django 4.0.2 on 2022-03-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Frequently Asked Questions',
            },
        ),
    ]
