# Generated by Django 5.1.4 on 2024-12-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_remove_group_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
