# Generated by Django 4.0.1 on 2022-02-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
