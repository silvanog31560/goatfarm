# Generated by Django 4.1.3 on 2022-11-25 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goat', '0010_alter_doe_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doe',
            name='gender',
        ),
    ]
