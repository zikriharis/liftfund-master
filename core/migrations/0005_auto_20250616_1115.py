# Generated by Django 5.0.10 on 2025-06-16 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
    ]