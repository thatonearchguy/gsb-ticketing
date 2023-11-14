# Generated by Django 4.2.6 on 2023-11-14 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0006_workerapplicationrole_workerapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='bus_destination',
            field=models.CharField(default='unselected', max_length=100),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_departure_bus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='workerapplicationrole',
            name='description',
            field=models.TextField(max_length=600),
        ),
    ]