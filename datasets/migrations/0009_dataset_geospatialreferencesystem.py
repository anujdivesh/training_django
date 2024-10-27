# Generated by Django 5.1.2 on 2024-10-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0008_dataset_boundingbox"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="geospatialReferenceSystem",
            field=models.CharField(default="EPSG:4326", max_length=255),
        ),
    ]
