# Generated by Django 4.0.6 on 2023-04-04 21:04

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="film_work_state",
            field=models.CharField(max_length=255, null=True, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="room",
            name="film_work_time",
            field=models.FloatField(null=True, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="room",
            name="film_work_uuid",
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "external_access_token",
                    models.CharField(default="", max_length=120, verbose_name="external_access_token"),
                ),
                (
                    "external_refresh_token",
                    models.CharField(default="", max_length=120, verbose_name="external_refresh_token"),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]