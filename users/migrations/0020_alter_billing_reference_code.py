# Generated by Django 5.1.4 on 2025-01-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_billing_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='reference_code',
            field=models.TextField(default='uaa8f2v7rpafy58kksvc'),
        ),
    ]
