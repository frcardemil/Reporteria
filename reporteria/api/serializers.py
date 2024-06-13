from rest_framework.serializers import ModelSerializer
from reporteria.models import ReporteGeneral

class ReporteSerializer(ModelSerializer):
    class Meta:
        model = ReporteGeneral
        fields = '__all__'