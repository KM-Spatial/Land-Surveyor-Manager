# Generated by Django 4.0.2 on 2022-04-04 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_billing_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='expire_date',
            field=models.DateField(default=datetime.date(2022, 5, 4)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='reference_code',
            field=models.TextField(default='6x19mrnjngupk4w9tv6o'),
        ),
    ]