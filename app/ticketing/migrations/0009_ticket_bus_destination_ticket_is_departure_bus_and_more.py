# Generated by Django 4.2.6 on 2023-12-07 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0008_remove_workerapplication_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerapplication',
            name='exp_desc',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='workerapplication',
            name='other_exp',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='workerapplication',
            name='qualities',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='workerapplication',
            name='reason',
            field=models.TextField(default='', max_length=2000),
        ),
    ]
