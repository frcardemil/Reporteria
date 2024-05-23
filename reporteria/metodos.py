import openpyxl
import os

def agregarReporte():
    # Crear un nuevo libro de trabajo y una hoja
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "MiHoja"

    carpeta = "excel_files"
    nombre = "reporte.xlsx"
    ruta = carpeta+"\\"+nombre

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Guardar el archivo
    wb.save(ruta)
    
    abrirReporte(ruta)

def abrirReporte(ruta):
    # Verificar que el archivo se haya guardado correctamente
    if os.path.exists(ruta):
        print(f"El archivo de la ruta '{ruta}' existe")
        # Abrir el archivo con la aplicación predeterminada
        os.startfile(ruta)
    else:
        print(f"El archivo de la ruta '{ruta}' No Existe")
