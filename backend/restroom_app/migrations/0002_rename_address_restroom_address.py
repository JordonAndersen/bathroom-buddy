# Generated by Django 5.0.6 on 2024-06-17 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restroom_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restroom',
            old_name='Address',
            new_name='address',
        ),
    ]
