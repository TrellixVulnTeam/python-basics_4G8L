# Generated by Django 2.2.4 on 2019-08-16 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_create',
            new_name='task_created',
        ),
    ]
