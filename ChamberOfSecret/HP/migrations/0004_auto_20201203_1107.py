# Generated by Django 3.1.4 on 2020-12-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HP', '0003_auto_20201203_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='positions',
            new_name='role',
        ),
    ]