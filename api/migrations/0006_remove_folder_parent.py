# Generated by Django 5.0.6 on 2024-07-10 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_folder_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='parent',
        ),
    ]