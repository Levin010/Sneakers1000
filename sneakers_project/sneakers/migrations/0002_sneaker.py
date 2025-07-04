# Generated by Django 5.2.3 on 2025-06-28 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sneakers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sneaker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="uploads/"),
                ),
                (
                    "thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="uploads/"),
                ),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sneakers",
                        to="sneakers.category",
                    ),
                ),
            ],
            options={
                "ordering": ("-date_added",),
            },
        ),
    ]
