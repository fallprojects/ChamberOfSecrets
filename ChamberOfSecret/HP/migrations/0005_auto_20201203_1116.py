# Generated by Django 3.1.4 on 2020-12-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HP', '0004_auto_20201203_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('Cleaner', 'Cleaner'), ('Manager', 'Manager'), ('System Admin', 'System Admin'), ('General Director', 'General Director'), ('Master', 'Master')], max_length=120),
        ),
    ]
