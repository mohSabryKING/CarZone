# Generated by Django 5.0 on 2024-05-14 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_user_model_has_petrol_user_model_has_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='has_petrol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='has_petrol', to='core.petrol_area'),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='has_school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='has_school', to='core.school_of_drive'),
        ),
    ]
