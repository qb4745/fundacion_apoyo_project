# Generated by Django 4.2.1 on 2023-07-10 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_planmedicacion_residente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dosismedicamento',
            old_name='dosis',
            new_name='dosis_diarias',
        ),
    ]
