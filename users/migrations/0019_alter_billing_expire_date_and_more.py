# Generated by Django 4.0.2 on 2025-01-12 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_billing_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='expire_date',
            field=models.DateField(default=datetime.date(2025, 2, 11)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='reference_code',
            field=models.TextField(default='s1ei8k0wfuelmh8njnpk'),
        ),
    ]
