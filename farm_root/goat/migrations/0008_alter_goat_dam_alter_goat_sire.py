# Generated by Django 4.1.3 on 2022-11-25 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goat', '0007_alter_goat_availability_alter_goat_dam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goat',
            name='dam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='damkids', to='goat.doe'),
        ),
        migrations.AlterField(
            model_name='goat',
            name='sire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sirekids', to='goat.buck'),
        ),
    ]
