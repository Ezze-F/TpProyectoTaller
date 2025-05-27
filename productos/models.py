# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Productos(models.Model):
    codigo = models.AutoField(db_column='codigo', primary_key=True)
    preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=10, decimal_places=0, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaelaboracion = models.DateField(db_column='fechaElaboracion', blank=True, null=True)
    fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'productos'
