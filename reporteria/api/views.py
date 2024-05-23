from rest_framework.viewsets import ModelViewSet
from reporteria.models import Reporte
from reporteria.api.serializers import ReporteSerializer

class ReporteApiViewSet(ModelViewSet):
    serializer_class = ReporteSerializer
    queryset = Reporte.objects.all()