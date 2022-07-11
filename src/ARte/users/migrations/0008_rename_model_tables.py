# Generated by Django 2.2.24 on 2021-06-20 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_delete_artwork2"),
        ("users", "0007_auto_20200220_1425"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="marker",
                    name="owner",
                ),
                migrations.RemoveField(
                    model_name="object",
                    name="owner",
                ),
            ],
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name="Artwork",
                ),
                migrations.DeleteModel(
                    name="Marker",
                ),
                migrations.DeleteModel(
                    name="Object",
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name="Artwork",
                    table="core_artwork",
                ),
                migrations.AlterModelTable(
                    name="Marker",
                    table="core_marker",
                ),
                migrations.AlterModelTable(
                    name="Object",
                    table="core_object",
                ),
            ],
        ),
    ]
