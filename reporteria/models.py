from django.db import models
from .metodos import ultimo_dia_del_mes

# Create your models here.

class ReporteGeneral(models.Model):
    mes_anno_reporte = models.DateField(verbose_name="Mes y Año del Reporte",primary_key=True) #Saber mes y año del reporte (Reporteria)
    entrega_total = models.IntegerField(default=1, verbose_name="Despachos efectuados") #Conocer cant. despachos hechos (Despacho)
    entrega_a_tiempo = models.IntegerField(default=1, verbose_name="Despachos a tiempo") #Conocer cant. depachos entregados cuando deberian (Despacho)
    stock_productos = models.IntegerField(default=1, verbose_name="Stock de productos") #Conocer stock final (Stock)
    pedido_proveedor = models.IntegerField(default=1, verbose_name="Pedidos a proveedores") #Conocer cant. pedidos hechos a proveedores (Proveedor)
    adquisicion_recibida = models.IntegerField(default=1, verbose_name="Adquisicion a tiempo") #Conocer cant. de adquisiciones hechas (Adquisicion)
    venta_pedido = models.IntegerField(default=1, verbose_name="Ventas pedidas") #Conocer cant. de ventas efectuadas (Post-Venta)
    venta_realizada = models.IntegerField(default=1, verbose_name="Ventas definitivas") #Conocer cant. de ventas sin anular o cancelar (Venta)
    factura_total = models.IntegerField(default=1, verbose_name="Facturas hechas en total") #Conocer cant. facturas hechas (Contabilidad)
    factura_pagada = models.IntegerField(default=1, verbose_name="Facturas pagadas") #Conocer cant. de facturas que fueron pagadas. (Contabilidad)

    def save(self, *args, **kwargs):
        if self.mes_anno_reporte:
            self.mes_anno_reporte = ultimo_dia_del_mes(self.mes_anno_reporte)
        super().save(*args, **kwargs)

    @property
    def mes(self):
        return self.mes_anno_reporte.month

    @property
    def año(self):
        return self.mes_anno_reporte.year

    def __str__(self):
        return f"{self.mes_anno_reporte.month}/{self.mes_anno_reporte.year}"
