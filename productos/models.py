# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# ChatGPT
from django.db import models
from django.utils import timezone

# Manager para productos no eliminados
class ProductoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

# Manager para productos eliminados
class ProductoDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)

class Productos(models.Model):
    codigo = models.AutoField(db_column='codigo', primary_key=True)
    preciounitario = models.DecimalField(
        db_column='precioUnitario', max_digits=10, decimal_places=2, blank=True, null=True
    )
    marca = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaelaboracion = models.DateField(db_column='fechaElaboracion', blank=True, null=True)
    fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Managers personalizados
    objects = ProductoManager()               # Solo productos no eliminados
    all_objects = models.Manager()            # Todos los productos
    deleted_objects = ProductoDeletedManager()  # Solo productos eliminados

    class Meta:
        managed = True
        db_table = 'productos'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

    def soft_delete(self):
        """Marca el producto como eliminado sin borrarlo físicamente."""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restaura un producto previamente eliminado lógicamente."""
        self.is_deleted = False
        self.deleted_at = None
        self.save()


# # productos/models.py
# from django.db import models
# from django.utils import timezone

# # Manager personalizado para productos no eliminados
# class ProductoManager(models.Manager):
#     def get_queryset(self):
#         # Por defecto, solo devuelve productos que NO estén eliminados
#         return super().get_queryset().filter(is_deleted=False)

# # Manager personalizado para productos eliminados
# class ProductoDeletedManager(models.Manager):
#     def get_queryset(self):
#         # Solo devuelve productos que SÍ estén eliminados
#         return super().get_queryset().filter(is_deleted=True)

# class Productos(models.Model): # <--- ¡Clase nombrada como Productos!
#     codigo = models.AutoField(db_column='codigo', primary_key=True)
#     preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=10, decimal_places=0, blank=True, null=True)
#     marca = models.CharField(max_length=100, blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     fechaelaboracion = models.DateField(db_column='fechaElaboracion', blank=True, null=True)
#     fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)
#     descripcion = models.CharField(max_length=100, blank=True, null=True)
#     is_deleted = models.BooleanField(default=False)
#     deleted_at = models.DateTimeField(null=True, blank=True)

#     # Asigna los managers personalizados
#     # Estos managers ahora operan sobre la clase 'Productos'
#     objects = ProductoManager()
#     all_objects = models.Manager()
#     deleted_objects = ProductoDeletedManager()
    
#     class Meta:
#         managed = True
#         db_table = 'productos' # Asegúrate de que el nombre de tu tabla de base de datos sea consistente

#     def __str__(self):
#         return f"{self.codigo} - {self.descripcion}"

#     def delete(self, *args, **kwargs):
#         self.is_deleted = True
#         self.deleted_at = timezone.now()
#         self.save()

#     def restore(self, *args, **kwargs):
#         self.is_deleted = False
#         self.deleted_at = None
#         self.save()



# from django.db import models
# from django.utils import timezone # Importa timezone para los métodos soft delete/restore

# # Manager personalizado para productos no eliminados
# class ProductoManager(models.Manager):
#     def get_queryset(self):
#         # Por defecto, solo devuelve productos que NO estén eliminados
#         return super().get_queryset().filter(is_deleted=False)

# # Manager personalizado para productos eliminados
# class ProductoDeletedManager(models.Manager):
#     def get_queryset(self):
#         # Solo devuelve productos que SÍ estén eliminados
#         return super().get_queryset().filter(is_deleted=True)

# class Productos(models.Model): # Mantén este nombre de clase como 'Producto'
#     codigo = models.AutoField(db_column='codigo', primary_key=True)
#     preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=10, decimal_places=0, blank=True, null=True)
#     marca = models.CharField(max_length=100, blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     fechaelaboracion = models.DateField(db_column='fechaElaboracion', blank=True, null=True)
#     fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)
#     descripcion = models.CharField(max_length=100, blank=True, null=True)
#     is_deleted = models.BooleanField(default=False)
#     deleted_at = models.DateTimeField(null=True, blank=True)

#     # Asigna los managers personalizados
#     objects = ProductoManager()           # Manager por defecto para ítems no eliminados
#     all_objects = models.Manager()        # Manager para obtener TODOS los ítems (eliminados o no)
#     deleted_objects = ProductoDeletedManager() # Manager para obtener SÓLO los ítems eliminados
    
#     class Meta:
#         managed = True
#         db_table = 'productos' # Asegúrate de que el nombre de tu tabla de base de datos sea consistente

#     def __str__(self):
#         return f"{self.codigo} - {self.descripcion}"

#     # Sobrescribe el método delete por defecto para realizar un soft delete
#     def delete(self, *args, **kwargs):
#         self.is_deleted = True
#         self.deleted_at = timezone.now()
#         self.save()

#     # Método para restaurar el producto
#     def restore(self, *args, **kwargs):
#         self.is_deleted = False
#         self.deleted_at = None
#         self.save()



# from django.db import models


# class Productos(models.Model):
#     codigo = models.AutoField(db_column='codigo', primary_key=True)
#     preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=10, decimal_places=0, blank=True, null=True)
#     marca = models.CharField(max_length=100, blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     fechaelaboracion = models.DateField(db_column='fechaElaboracion', blank=True, null=True)
#     fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)
#     descripcion = models.CharField(max_length=100, blank=True, null=True)
#     is_deleted = models.BooleanField(default=False) # Nuevo campo para soft delete
#     deleted_at = models.DateTimeField(null=True, blank=True) # Opcional: para registrar cuándo se eliminó
    
#     class Meta:
#         managed = True
#         db_table = 'productos'

#     def __str__(self):
#         return f"{self.codigo} - {self.descripcion}"

#     # Opcional: sobreescribe el método delete para que realice un soft delete
#     def delete(self, *args, **kwargs):
#         from django.utils import timezone
#         self.is_deleted = True
#         self.deleted_at = timezone.now()
#         self.save()

#     # Método para restaurar el producto
#     def restore(self, *args, **kwargs):
#         self.is_deleted = False
#         self.deleted_at = None
#         self.save()

# # Puedes crear un manager personalizado para facilitar las consultas
# class ProductoManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_deleted=False)

# class ProductoDeletedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_deleted=True)

# # Y luego en tu modelo
# class Producto(models.Model):
#     # ... tus campos existentes ...
#     is_deleted = models.BooleanField(default=False)
#     deleted_at = models.DateTimeField(null=True, blank=True)

#     objects = ProductoManager() # Manager por defecto, solo muestra los no eliminados
#     all_objects = models.Manager() # Manager para todos (eliminados y no eliminados)
#     deleted_objects = ProductoDeletedManager() # Manager para solo los eliminados

#     def delete(self, *args, **kwargs):
#         from django.utils import timezone
#         self.is_deleted = True
#         self.deleted_at = timezone.now()
#         self.save()

#     def restore(self, *args, **kwargs):
#         self.is_deleted = False
#         self.deleted_at = None
#         self.save()

#     # ... tu método __str__ ...