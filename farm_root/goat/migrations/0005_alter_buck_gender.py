# Generated by Django 4.1.3 on 2022-11-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goat', '0004_alter_goat_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buck',
            name='gender',
            field=models.CharField(choices=[('BUCK', 'Buck'), ('WETHER', 'Wether')], default='BUCK', max_length=6),
        ),
    ]
