# Generated by Django 3.0.4 on 2020-03-31 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0002_cheese_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheese',
            name='slug',
        ),
    ]
