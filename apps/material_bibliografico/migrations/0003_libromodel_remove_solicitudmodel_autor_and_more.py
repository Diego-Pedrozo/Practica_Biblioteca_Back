# Generated by Django 4.0.5 on 2024-04-30 11:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material_bibliografico', '0002_alter_solicitudmodel_anotacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('autor', models.CharField(max_length=50, verbose_name='Autor/es')),
                ('editorial', models.CharField(max_length=50, verbose_name='Editorial')),
                ('edicion', models.CharField(max_length=50, verbose_name='Edición')),
                ('ejemplares', models.IntegerField(verbose_name='Ejemplares')),
                ('fecha_publicacion', models.DateField(max_length=50, verbose_name='Fecha de publicación')),
                ('idioma', models.CharField(choices=[('Español', 'Español'), ('Ingles', 'Ingles')], default='', max_length=50, verbose_name='Idioma')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.RemoveField(
            model_name='solicitudmodel',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='solicitudmodel',
            name='edicion',
        ),
        migrations.RemoveField(
            model_name='solicitudmodel',
            name='editorial',
        ),
        migrations.RemoveField(
            model_name='solicitudmodel',
            name='ejemplares',
        ),
        migrations.RemoveField(
            model_name='solicitudmodel',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='solicitudmodel',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='solicitudmodel',
            name='titulo',
        ),
        migrations.AddField(
            model_name='solicitudmodel',
            name='fecha_solicitud',
            field=models.DateField(blank=True, default=datetime.date.today, max_length=50, verbose_name='Fecha de solicitud'),
        ),
        migrations.AddField(
            model_name='solicitudmodel',
            name='nivel_revision',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=50, verbose_name='Nivel de revisión'),
        ),
        migrations.AddField(
            model_name='solicitudmodel',
            name='libro',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='libro', to='material_bibliografico.libromodel', verbose_name='Libro'),
        ),
    ]
