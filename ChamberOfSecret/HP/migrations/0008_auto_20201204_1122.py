# Generated by Django 3.1.4 on 2020-12-04 11:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('HP', '0007_auto_20201203_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='role2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'no rights'), (2, 'Cleaner'), (3, 'Manager'), (4, 'System Admin'), (5, 'General Director'), (6, 'Master')], default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('no rights', 'no rights'), ('Cleaner', 'Cleaner'), ('Manager', 'Manager'), ('System Admin', 'System Admin'), ('General Director', 'General Director'), ('Master', 'Master')], max_length=120),
        ),
    ]
