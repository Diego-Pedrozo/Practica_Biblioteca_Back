# Generated by Django 4.0.5 on 2024-06-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_userinformationmodel_user_facultad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformationmodel',
            name='user_type',
            field=models.CharField(choices=[('1', 'Administrador'), ('2', 'Director plan de estudios'), ('3', 'Director de departamento'), ('4', 'Decano'), ('5', 'Biblioteca')], help_text='Seleccione un tipo de usuario', max_length=255, verbose_name='Tipo de usuario'),
        ),
    ]
