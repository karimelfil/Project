# Generated by Django 5.0.6 on 2024-05-27 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wieght',
        ),
    ]
