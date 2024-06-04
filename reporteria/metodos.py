import openpyxl
import os

from datetime import timedelta

def ultimo_dia_del_mes(fecha):
    if fecha.month == 12:
        return fecha.replace(day=31)
    siguiente_mes = fecha.replace(month=fecha.month + 1, day=1)
    return siguiente_mes - timedelta(days=1)

carpeta = "media\\excel_files"

def agregarReporte(pNombre,openRt):
    # Crear un nuevo libro de trabajo y una hoja
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "MiHoja"

    nombre = pNombre+".xlsx"
    ruta = carpeta+"\\"+nombre

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ws['A1'] = 'Productos'
    ws['A2'] = 'Teclado'
    ws['A3'] = 'Mouse'
    ws['A4'] = 'Monitor'
    
    ws['B1'] = 'Precio'
    ws['B2'] = 1000
    ws['B3'] = 2000
    ws['B4'] = 3000

    # Guardar el archivo
    wb.save(ruta)
    if openRt:
        abrirReporte(ruta)

def abrirReporte(ruta):
    # Verificar que el archivo se haya guardado correctamente
    if os.path.exists(ruta):
        print(f"El archivo de la ruta '{ruta}' existe")
        # Abrir el archivo con la aplicación predeterminada
        os.startfile(ruta)
    else:
        print(f"El archivo de la ruta '{ruta}' No Existe")

def excel_a_lista(archivo_excel):
    # Cargar el archivo Excel
    workbook = openpyxl.load_workbook(filename=archivo_excel)
    
    # Seleccionar la primera hoja del libro de trabajo
    sheet = workbook.active
    
    # Crear una lista para almacenar los datos
    datos = []
    
    # Iterar sobre las filas de la hoja y agregar cada fila a la lista de datos
    for row in sheet.iter_rows(values_only=True):
        fila = [cell for cell in row]
        datos.append(fila)
    return datos


