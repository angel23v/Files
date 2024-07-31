# Generated by Django 5.0.6 on 2024-07-10 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_folder_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.folder'),
        ),
    ]
