# Generated by Django 3.2.12 on 2022-10-11 16:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0078_experiencepage_liked_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="experiencepage",
            name="likes",
        ),
    ]
