# Generated by Django 5.0.4 on 2024-05-07 01:09

from django.db import migrations


def populate_status(apps, schemaeditro):
    entries = {
        "draft": "A post that is not ready to be published",
        "published": "A post available for all to see",
        "archived": "An older post available in the archive only",
    }
    Status = apps.get_model("posts", "Status")
    for key, vaule in entries.items():
        status_obj = Status(name=key, description=vaule)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [migrations.RunPython(populate_status)]
