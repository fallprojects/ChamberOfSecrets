# Generated by Django 3.1.4 on 2020-12-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HP', '0012_auto_20201208_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='mark',
            field=models.CharField(choices=[('all', 'all'), ('managers', 'managers'), ('middle', 'middle'), ('secret', 'secret'), ('top secret', 'top secret')], max_length=100),
        ),
    ]
