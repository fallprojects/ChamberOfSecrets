# Generated by Django 3.1.4 on 2020-12-08 12:49

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('HP', '0011_auto_20201204_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='mark',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('all', 'all'), ('managers', 'managers'), ('middle', 'middle'), ('secret', 'secret'), ('top secret', 'top secret')], max_length=100),
        ),
    ]