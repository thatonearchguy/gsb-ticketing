# Generated by Django 4.1 on 2022-11-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticketing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="date_paid",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
