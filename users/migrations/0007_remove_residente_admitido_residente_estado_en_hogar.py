# Generated by Django 4.2.1 on 2023-06-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_residente_admitido_residente_fecha_admision_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="residente",
            name="admitido",
        ),
        migrations.AddField(
            model_name="residente",
            name="estado_en_hogar",
            field=models.CharField(
                choices=[("I", "Ingresado/a"), ("E", "Egresado/a")],
                default="I",
                max_length=1,
            ),
        ),
    ]
