# Generated by Django 4.0.5 on 2024-05-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_bibliografico', '0011_publicacionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudmodel',
            name='nivel_revision',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=50, verbose_name='Nivel de revisión'),
        ),
    ]
