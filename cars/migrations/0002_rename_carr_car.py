# Generated by Django 5.1.3 on 2024-12-10 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carr',
            new_name='Car',
        ),
    ]
