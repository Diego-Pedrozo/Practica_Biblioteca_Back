# Generated by Django 4.0.5 on 2024-05-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_userinformationmodel_user_facultad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformationmodel',
            name='user_facultad',
            field=models.CharField(blank=True, choices=[('1', 'Ciencias Agrarias y del Ambiente'), ('2', 'Ciencias Básicas'), ('3', 'Ciencias Empresariales'), ('4', 'Ciencias de salud'), ('5', 'Educación, Artes y Humanidades'), ('6', 'Ingeniería')], help_text='Seleccione una facultad', max_length=255, null=True, verbose_name='Facultad'),
        ),
        migrations.AlterField(
            model_name='userinformationmodel',
            name='user_programa',
            field=models.CharField(blank=True, choices=[('1', 'Ingeniería Agroindustrial'), ('2', 'Ingeniería Agronómica'), ('3', 'Ingeniería Ambiental'), ('4', 'Ingeniería Biotecnológica'), ('5', 'Zootecnia'), ('6', 'Química Industrial'), ('7', 'Administración de Empresas'), ('8', 'Contaduría Pública'), ('9', 'Comercio Internacional'), ('10', 'Enfermería'), ('11', 'Seguridad y Salud en el Trabajo'), ('12', 'Comunicación Social'), ('13', 'Trabajo Social'), ('14', 'Derecho'), ('15', 'Arquitectura'), ('16', 'Ingeniería Civil'), ('17', 'Ingeniería de Sistemas'), ('18', 'Ingeniería Electrónica'), ('19', 'Ingeniería Electromecánica'), ('20', 'Ingeniería Industrial'), ('21', 'Ingeniería de Minas'), ('22', 'Ingeniería Mecánica')], help_text='Seleccione un programa academico', max_length=255, null=True, verbose_name='Programa academico'),
        ),
    ]
