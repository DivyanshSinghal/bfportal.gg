# Generated by Django 3.2.11 on 2022-01-17 19:29

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
        ("core", "0011_remove_experiencepage_core_experiencepage_code_or_exp_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfilePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
    ]
