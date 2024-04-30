# Generated by Django 4.0.5 on 2024-04-30 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material_bibliografico', '0003_libromodel_remove_solicitudmodel_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudmodel',
            name='libro',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='libro', to='material_bibliografico.libromodel', verbose_name='Libro'),
        ),
    ]
