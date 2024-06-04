from rest_framework.viewsets import ModelViewSet
from reporteria.models import ReporteGeneral
from reporteria.api.serializers import ReporteSerializer

class ReporteApiViewSet(ModelViewSet):
    serializer_class = ReporteSerializer
    queryset = ReporteGeneral.objects.all()