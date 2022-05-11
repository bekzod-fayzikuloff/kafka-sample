# Generated by Django 4.0.4 on 2022-05-10 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[("Rev", "Review"), ("Blo", "Blocked"), ("Cor", "Correct")], default="Rev", max_length=3
                    ),
                ),
            ],
            options={
                "verbose_name": "message",
                "verbose_name_plural": "messages",
            },
        ),
    ]