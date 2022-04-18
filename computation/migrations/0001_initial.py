# Generated by Django 4.0.2 on 2022-04-18 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Polar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(blank=True, max_length=200, null=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('distance', models.FloatField()),
                ('direction', models.CharField(max_length=200)),
                ('end_name', models.CharField(blank=True, max_length=200, null=True)),
                ('x_coordinate', models.FloatField(blank=True, null=True)),
                ('y_coordinate', models.FloatField(blank=True, null=True)),
                ('stored_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Calculated Polars',
            },
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_name', models.CharField(blank=True, max_length=200, null=True)),
                ('y_start', models.FloatField()),
                ('x_start', models.FloatField()),
                ('end_name', models.CharField(blank=True, max_length=200, null=True)),
                ('y_end', models.FloatField()),
                ('x_end', models.FloatField()),
                ('distance', models.FloatField(blank=True, null=True)),
                ('direction_dd', models.FloatField(blank=True, null=True)),
                ('direction_deg', models.IntegerField(blank=True, null=True)),
                ('direction_min', models.IntegerField(blank=True, null=True)),
                ('direction_sec', models.FloatField(blank=True, null=True)),
                ('stored_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Calculated Joins',
            },
        ),
    ]
