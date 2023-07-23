# Generated by Django 4.1.7 on 2023-04-21 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("core", "0079_remove_experiencepage_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experiencepagetag",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_items",
                to="taggit.tag",
            ),
        ),
    ]
