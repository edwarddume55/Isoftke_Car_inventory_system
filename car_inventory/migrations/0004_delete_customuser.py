# Generated by Django 5.0.4 on 2024-04-06 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_inventory', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]