# Generated by Django 5.1.2 on 2024-10-23 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0002_dataset_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dataset",
            name="file_record",
        ),
    ]
