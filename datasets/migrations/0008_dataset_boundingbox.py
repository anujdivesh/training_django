# Generated by Django 5.1.2 on 2024-10-24 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boundingbox", "0001_initial"),
        ("datasets", "0007_rename_spatialrepresentationinfo_dataset_spatialinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="boundingBox",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="boundingBox_id",
                to="boundingbox.boundingbox",
            ),
            preserve_default=False,
        ),
    ]
