# Generated by Django 5.1.2 on 2024-10-24 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boundingbox", "0001_initial"),
        ("datasets", "0011_dataset_license_dataset_publisher"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="LocalAccessPath",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="dataset",
            name="Tag",
            field=models.CharField(default="satellite", max_length=255),
        ),
        migrations.AddField(
            model_name="dataset",
            name="Topic",
            field=models.CharField(default="Oceans", max_length=255),
        ),
        migrations.AlterField(
            model_name="dataset",
            name="boundingBox",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="boundingBox_id",
                to="boundingbox.boundingbox",
            ),
        ),
    ]
