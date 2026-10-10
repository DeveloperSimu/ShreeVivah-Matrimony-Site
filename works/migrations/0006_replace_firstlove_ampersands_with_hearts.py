import re

from django.db import migrations


def replace_ampersands_with_hearts(apps, schema_editor):
    Firstlook = apps.get_model("works", "Firstlook")
    database = schema_editor.connection.alias
    for story in Firstlook.objects.using(database).only("pk", "title").iterator():
        updated_title = re.sub(r"\s*&\s*", " ❤️ ", story.title).strip()
        if updated_title != story.title:
            Firstlook.objects.using(database).filter(pk=story.pk).update(
                title=updated_title
            )


def restore_ampersands(apps, schema_editor):
    Firstlook = apps.get_model("works", "Firstlook")
    database = schema_editor.connection.alias
    for story in Firstlook.objects.using(database).only("pk", "title").iterator():
        updated_title = re.sub(r"\s*❤️\s*", " & ", story.title).strip()
        if updated_title != story.title:
            Firstlook.objects.using(database).filter(pk=story.pk).update(
                title=updated_title
            )


class Migration(migrations.Migration):
    dependencies = [
        ("works", "0005_manage_existing_firstlove_stories"),
    ]

    operations = [
        migrations.RunPython(
            replace_ampersands_with_hearts,
            restore_ampersands,
        ),
    ]
