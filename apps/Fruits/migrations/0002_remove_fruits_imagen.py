# Generated by Django 3.2.8 on 2022-11-13 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fruits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruits',
            name='imagen',
        ),
    ]
