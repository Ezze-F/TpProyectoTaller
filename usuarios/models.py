from django.db import models

# Create your models here.

class Usuarios(models.Model):
    codigo = models.AutoField(db_column='codigo', primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    clave = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'usuarios'