# Generated by Django 3.2.11 on 2022-01-14 18:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailforms", "0004_add_verbose_name_plural"),
        ("wagtailcore", "0066_collection_management_permissions"),
        ("wagtailredirects", "0006_redirect_increase_max_length"),
        ("core", "0005_experiencesubmitpage"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ExperienceSubmitPage",
        ),
    ]
