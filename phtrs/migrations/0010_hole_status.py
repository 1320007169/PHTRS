# Generated by Django 4.2.6 on 2023-11-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phtrs", "0009_hole"),
    ]

    operations = [
        migrations.AddField(
            model_name="hole",
            name="status",
            field=models.CharField(
                choices=[
                    ("work in progress", "work in progress"),
                    ("repaired", "repaired"),
                    ("temporary repair", "temporary repair"),
                    ("not repair", "not repair"),
                ],
                default="not repair",
                max_length=30,
            ),
        ),
    ]
