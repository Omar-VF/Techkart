# Generated by Django 5.0.2 on 2024-03-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_rename_name_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=0),
        ),
    ]
