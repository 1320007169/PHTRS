# Generated by Django 4.2.6 on 2023-11-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phtrs", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ward",
            old_name="NurseId",
            new_name="assignedNurseId",
        ),
        migrations.AddField(
            model_name="ward",
            name="isAssigned",
            field=models.BooleanField(default=False),
        ),
    ]