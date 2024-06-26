# Generated by Django 4.0.5 on 2024-05-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_bibliografico', '0010_alter_solicitudmodel_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicacionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='publicaciones/', verbose_name='Imagen')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]
