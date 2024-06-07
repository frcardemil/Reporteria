from rest_framework.serializers import ModelSerializer
from reporteria.models import ReporteGeneral

class ReporteSerializer(ModelSerializer):
    class Meta:
        model = ReporteGeneral
        fields = ['anno_mes_rt','entrega_total','entrega_a_tiempo','stock_productos','pedido_proveedor',
                  'adquisicion_recibida','venta_pedido','venta_realizada','factura_total','factura_pagada']