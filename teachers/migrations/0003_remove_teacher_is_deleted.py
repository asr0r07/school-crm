# Generated by Django 5.1.4 on 2024-12-28 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_remove_teacher_science'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='is_deleted',
        ),
    ]
