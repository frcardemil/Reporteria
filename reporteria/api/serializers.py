from rest_framework.serializers import ModelSerializer
from reporteria.models import Reporte

class ReporteSerializer(ModelSerializer):
    class Meta:
        model = Reporte
        fields = ['id','razon','reporte','id_area','fecha_Emision','margen_fecha_datos']