# Generated by Django 5.1.2 on 2024-10-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="file",
            field=models.FileField(default=1, upload_to="uploads/"),
            preserve_default=False,
        ),
    ]
