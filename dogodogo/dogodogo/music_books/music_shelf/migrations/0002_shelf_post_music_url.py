# Generated by Django 4.2.11 on 2024-04-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music_shelf", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shelf_post", name="music_url", field=models.URLField(null=True),
        ),
    ]
