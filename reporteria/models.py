from django.db import models
from . import metodos  

# Create your models here.

class ReporteGeneral(models.Model):
    anno_mes_rt = models.IntegerField(verbose_name="Año y Mes del Reporte",primary_key=True) #Saber año y mes del reporte (Reporteria)
    entrega_total = models.IntegerField(default=1, verbose_name="Despachos efectuados") #Conocer cant. despachos hechos (Despacho)
    entrega_a_tiempo = models.IntegerField(default=1, verbose_name="Despachos a tiempo") #Conocer cant. depachos entregados cuando deberian (Despacho)
    stock_productos = models.IntegerField(default=1, verbose_name="Stock de productos") #Conocer stock final (Stock)
    pedido_proveedor = models.IntegerField(default=1, verbose_name="Pedidos a proveedores") #Conocer cant. de productos de los proveedores (Proveedor)
    adquisicion_recibida = models.IntegerField(default=1, verbose_name="Adquisicion a tiempo") #Conocer cant. de adquisiciones hechas (Adquisicion)
    venta_pedido = models.IntegerField(default=1, verbose_name="Ventas pedidas") #Conocer cant. de ventas efectuadas (Post-Venta)
    venta_realizada = models.IntegerField(default=1, verbose_name="Ventas definitivas") #Conocer cant. de ventas sin anular o cancelar (Venta)
    factura_total = models.IntegerField(default=1, verbose_name="Facturas hechas en total") #Conocer cant. facturas hechas (Contabilidad)
    factura_pagada = models.IntegerField(default=1, verbose_name="Facturas pagadas") #Conocer cant. de facturas que fueron pagadas. (Contabilidad)
    boleta_total = models.IntegerField(default=1, verbose_name="Boletas hechas en total") #Conocer cant. boletas hechas (Contabilidad)
    boleta_pagada = models.IntegerField(default=1, verbose_name="Boletas pagadas") #Conocer cant. de boletas que fueron pagadas. (Contabilidad)

    def formato_anno_mes(self):
        anno_mes_tmp = str(self.anno_mes_rt)
        if len(anno_mes_tmp) >= 6:
            return f"{anno_mes_tmp[-2:]}/{anno_mes_tmp[:4]}"
        else:
            return "Formato inválido"
        
    def save(self, *args, **kwargs):
        metodos.agregarReporte('RT-'+str(self.anno_mes_rt),False,self)
        print('hola')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.formato_anno_mes()
