from django.db import models
from django.utils import timezone

# Manejador para productos no eliminados
class ProductoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

# Manejador para productos eliminados
class ProductoDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)

class Productos(models.Model):
    codigo = models.AutoField(db_column='codigo', primary_key=True)
    preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=10, decimal_places=2, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaelaboracion = models.DateField(db_column='fechaElaboracion', blank=True, null=True)
    fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Manejadores personalizados
    objects = ProductoManager() # sólo productos no eliminados.
    all_objects = models.Manager() # todos los productos.
    deleted_objects = ProductoDeletedManager() # sólo productos eliminados.

    class Meta:
        managed = True
        db_table = 'productos'

    def __str__(self):
        # Método para retornar una cadena de texto con el código y descripción de un registro
        return f"{self.codigo} - {self.descripcion}"

    def soft_delete(self):
        # Método para marcar el producto como eliminado sin borrarlo físicamente.
        self.is_deleted = True # se cambia el valor del atributo is_deleted de falso a verdadero (para que luego se muestre en la sección de eliminados)
        self.deleted_at = timezone.now() # se obtiene la fecha y hora exacta para guardala en el atributo deleted_at
        self.save() # se guardan los cambios

    def restore(self):
        # Método para restaurar un producto eliminado lógicamente.
        self.is_deleted = False # se cambia el valor del atributo is_deleted de verdadero a falso (para que luego se muestre en la sección de no eliminados)
        self.deleted_at = None # se modifica el atributo deleted_at con "nada"
        self.save() # se guardan los cambios