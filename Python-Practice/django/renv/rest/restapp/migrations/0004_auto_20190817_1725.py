# Generated by Django 2.2.4 on 2019-08-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_auto_20190816_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Images/None/No0img.jpg', upload_to='Images/'),
        ),
    ]
