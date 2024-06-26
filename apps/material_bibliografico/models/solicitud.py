from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from datetime import date
from apps.user.choices import UserRanges, UserFacultad, UserPrograma, NivelRevision

class LibroModel(models.Model):
    #info libro
    titulo = models.CharField(max_length=250, verbose_name=_('Título'), help_text=_(''), null=False, unique=False)
    autor = models.CharField(max_length=150, verbose_name=_('Autor/es'), help_text=_(''), null=False, unique=False)
    editorial = models.CharField(max_length=50, verbose_name=_('Editorial'), help_text=_(''), null=False, unique=False)
    edicion = models.CharField(max_length=50, verbose_name=_('Edición'), help_text=_(''), null=False, unique=False)
    ejemplares = models.IntegerField(verbose_name=_('Ejemplares'), help_text=_(''), null=False, unique=False)
    fecha_publicacion = models.IntegerField(verbose_name=_('Fecha de publicación'), help_text=_(''), null=False, unique=False)
    IDIOMA_CHOICES = [
        ('Español', 'Español'),
        ('Ingles', 'Ingles'),
    ] 
    idioma = models.CharField(max_length=50, verbose_name=_('Idioma'), help_text=_(''), choices=IDIOMA_CHOICES, default='', null=False, unique=False)

    def __str__(self) -> str:
        return f'{self.id}, {self.titulo}'
    
    class Meta:
        verbose_name = _('Libro')
        verbose_name_plural= _('Libros')
    

class SolicitudModel(models.Model):
    #info solicitud
    libro = models.ForeignKey(LibroModel, verbose_name=_("Libro"), on_delete=models.CASCADE, null=False, unique=False, related_name='libro')
    fecha_solicitud = models.DateField(max_length=50, verbose_name=_('Fecha de solicitud'), help_text=_(''), null=False, unique=False, default=date.today)
    facultad = models.CharField(max_length=300, verbose_name=_('Facultad'), help_text=_(''), choices=UserFacultad.choices, null=False, unique=False)
    programa_academico = models.CharField(max_length=300, verbose_name=_('Programa académico'), help_text=_(''), choices=UserPrograma.choices, null=False, unique=False)
    anotacion = models.CharField(max_length=300, verbose_name=_('Anotación'), help_text=_(''), null=False, default='No aplica', unique=False, blank= True)
    SOLICITANTE_CHOICES = [
        ('Estudiante', 'Estudiante'),
        ('Docente', 'Docente'),
    ] 
    solicitante = models.CharField(max_length=50, verbose_name=_('Solicitante'), help_text=_(''), choices=SOLICITANTE_CHOICES, default='', null=False, unique=False)
    email_solicitante = models.EmailField(verbose_name=_('Email solicitante'), help_text=_(''), default='', null=False, unique=False)

    #info verificacion
    ESTADO_CHOICES = [
        ('Existente', 'Existente'),
        ('En tramite', 'En trámite'),
        ('Inexistente', 'Inexistente'),
        ('Sin revisar', 'Sin revisar')
    ]
    estado = models.CharField(max_length=50, verbose_name=_('Estado'), help_text=_(''), choices=ESTADO_CHOICES, default='Sin revisar', null=False, unique=False)
    nivel_revision = models.CharField(max_length=50, verbose_name=_('Nivel de revisión'), help_text=_(''), choices=NivelRevision.choices, default='1', null=False, unique=False)

    def __str__(self) -> str:
        return f'{self.id}, {self.libro}, {self.fecha_solicitud}, {self.estado}, {self.nivel_revision}'
    
    class Meta:
        verbose_name = _('Solicitud')
        verbose_name_plural= _('Solicitudes')

