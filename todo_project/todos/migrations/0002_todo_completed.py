# Generated by Django 4.1.5 on 2023-01-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
