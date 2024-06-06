from django.db import models

class ReporteDespacho(models.Model):
    cantidad_de_despachos = models.IntegerField()
    entregados = models.IntegerField()
    no_entregados = models.IntegerField()

    def __str__(self):
        return f"Resumen {self.id}: {self.cantidad_de_despachos} despachos, {self.entregados} entregados, {self.no_entregados} no entregados"