# Generated by Django 4.2.7 on 2024-04-06 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ad",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "объявление",
                "verbose_name_plural": "объявления",
            },
        ),
        migrations.AlterField(
            model_name="review",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 6, 11, 53, 55, 421426),
                verbose_name="дата публиувции отзыва",
            ),
        ),
    ]