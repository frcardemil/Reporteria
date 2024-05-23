from django.db import models

class Reporte(models.Model):
    nombre_producto = models.CharField(max_length=100)
    stock_producto = models.IntegerField()
    fecha_despacho = models.DateField()
    proveedor = models.CharField(max_length=100)
    adquisiciones = models.TextField()
    postventa = models.TextField()
    contabilidad = models.TextField()

    def __str__(self):
        return self.nombre_producto
