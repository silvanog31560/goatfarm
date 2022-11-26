# Generated by Django 4.1.3 on 2022-11-25 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goat', '0006_alter_doe_bred_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goat',
            name='availability',
            field=models.CharField(choices=[('YES', 'Available'), ('NO', 'Not Available'), ('PENDING', 'Pending'), ('SOON', 'Coming Soon')], default='NO', max_length=7),
        ),
        migrations.AlterField(
            model_name='goat',
            name='dam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dambuckling', to='goat.doe'),
        ),
        migrations.AlterField(
            model_name='goat',
            name='sire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sirebuckling', to='goat.buck'),
        ),
        migrations.AlterField(
            model_name='goat',
            name='test_result',
            field=models.CharField(choices=[('POSITIVE', 'Positive'), ('NEGATIVE', 'Negative'), ('NOT', 'Not Tested')], default='NEGATIVE', max_length=8),
        ),
    ]
