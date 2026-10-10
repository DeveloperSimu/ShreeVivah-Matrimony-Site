from django.db import migrations


def seed_curated_profiles(apps, schema_editor):
    from profiles.profile_data import EXTRA_PROFILES, FEATURED_PROFILES

    CuratedProfile = apps.get_model("main", "CuratedProfile")
    database = schema_editor.connection.alias

    for profile in (*FEATURED_PROFILES, *EXTRA_PROFILES):
        CuratedProfile.objects.using(database).get_or_create(
            slug=profile["slug"],
            defaults={
                "gender": profile["gender"],
                "name": profile["name"],
                "profession": profile["profession"],
                "location": profile["location"],
                "about": profile["about"],
                "expectations": profile["expectations"],
                "family": profile["family"],
                "image_path": profile["photo"],
                "is_featured": profile in FEATURED_PROFILES,
            },
        )


def remove_seeded_curated_profiles(apps, schema_editor):
    from profiles.profile_data import EXTRA_PROFILES, FEATURED_PROFILES

    CuratedProfile = apps.get_model("main", "CuratedProfile")
    database = schema_editor.connection.alias
    slugs = [profile["slug"] for profile in (*FEATURED_PROFILES, *EXTRA_PROFILES)]
    CuratedProfile.objects.using(database).filter(slug__in=slugs).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_curatedprofile"),
    ]

    operations = [
        migrations.RunPython(seed_curated_profiles, remove_seeded_curated_profiles),
    ]
