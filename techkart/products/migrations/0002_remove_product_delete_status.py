# Generated by Django 5.0.2 on 2024-03-07 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='delete_status',
        ),
    ]
