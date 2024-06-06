from rest_framework import serializers
from .models import ReporteDespacho

class ReporteDespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteDespacho
        fields = '__all__'


