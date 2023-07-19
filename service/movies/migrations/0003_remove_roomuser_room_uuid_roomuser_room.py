# Generated by Django 4.0.6 on 2023-04-05 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "movies",
            "0002_alter_room_film_work_state_alter_room_film_work_time_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="roomuser",
            name="room_uuid",
        ),
        migrations.AddField(
            model_name="roomuser",
            name="room",
            field=models.ForeignKey(
                db_column="room_uuid",
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="movies.room",
            ),
            preserve_default=False,
        ),
    ]
