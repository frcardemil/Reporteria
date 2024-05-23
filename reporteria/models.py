from django.db import models

# Create your models here.

class Reporte(models.Model):
    razon = models.CharField(verbose_name='Razón',max_length=25)
    reporte = models.FileField(upload_to='excel_files/',null=False)
    id_area = models.ForeignKey('Area',on_delete=models.CASCADE,db_column='idArea',verbose_name='Área')
    fecha_Emision = models.DateField(blank=False,null=False,verbose_name='Fecha Emisión')
    margen_fecha_datos = models.CharField(max_length=40,blank=False,null=False,verbose_name='Margen de fecha de datos')
    
    def __str__(self):
        return str(self.razon)

class Area(models.Model):
    id_area = models.AutoField(db_column='idArea', primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return str(self.nombre)