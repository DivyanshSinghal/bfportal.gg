# Generated by Django 3.2.12 on 2022-10-11 09:41

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0065_auto_20221011_0928"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventspage",
            name="event",
            field=wagtail.fields.StreamField(
                [
                    (
                        "name",
                        wagtail.blocks.CharBlock(
                            help_text="Name of the event (only for admin panel)"
                        ),
                    ),
                    (
                        "event_link",
                        wagtail.blocks.URLBlock(help_text="URL of the event"),
                    ),
                ],
                blank=True,
                use_json_field=None,
            ),
        ),
    ]