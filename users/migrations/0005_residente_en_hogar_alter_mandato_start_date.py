# Generated by Django 4.2.1 on 2023-06-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_residente_fichamedica"),
    ]

    operations = [
        migrations.AddField(
            model_name="residente",
            name="en_hogar",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="mandato",
            name="start_date",
            field=models.DateField(),
        ),
    ]
