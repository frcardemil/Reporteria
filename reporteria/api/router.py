from rest_framework.routers import DefaultRouter
from reporteria.api.views import ReporteApiViewSet

router_reporte = DefaultRouter()

router_reporte.register(prefix='reporte',basename='reporte',viewset=ReporteApiViewSet)