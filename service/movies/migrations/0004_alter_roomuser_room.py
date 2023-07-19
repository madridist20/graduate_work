# Generated by Django 4.0.6 on 2023-04-05 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_remove_roomuser_room_uuid_roomuser_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomuser",
            name="room",
            field=models.ForeignKey(
                db_column="room_uuid", null=True, on_delete=django.db.models.deletion.CASCADE, to="movies.room"
            ),
        ),
    ]