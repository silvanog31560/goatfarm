# Generated by Django 4.1.3 on 2022-11-20 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goat', '0005_alter_buck_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doe',
            name='bred_status',
            field=models.CharField(choices=[('BRED', 'Bred'), ('OPEN', 'Open')], default='OPEN', max_length=4),
        ),
    ]