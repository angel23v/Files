# Generated by Django 5.0.6 on 2024-07-10 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_folder_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='folder',
        ),
    ]
