# Generated by Django 4.1.2 on 2022-11-06 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_supervisorreqs_issuperuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supervisorreqs',
            old_name='isSuperUser',
            new_name='isSupervisor',
        ),
    ]