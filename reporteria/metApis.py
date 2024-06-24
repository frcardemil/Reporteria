import requests
from datetime import datetime

#44.218.227.202
#34.224.245.239

apisHosts = {
    'adquisiciones' : '34.199.103.123:8000',
    'proveedor' : '0.0.0.0:8000',
    'ventas' : '0.0.0.0:8000',
    'despacho' : '44.205.221.190:8000',
    'post_venta' : '44.220.241.211:8000',
    'contabilidad' : '54.159.228.5:8000',
    'stock' : '0.0.0.0:8000',
    'reporteria' : '44.218.227.202:8000',
    'seguridad' : '0.0.0.0:8000',
}

def reporteriaApi():
    url = 'http://'+apisHosts['reporteria']+'/reporteria/api/reporte/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

def adquisicionesApi():
    url = 'http://'+apisHosts['adquisiciones']+'/api/v1/productos/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

"""
No poseo ruta exacta de proveedor

def proveedorApi():
    url = 'http://'+apisHosts['proveedor']+'/proveedor/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

"""
No poseo ruta exacta de ventas

def ventasApi():
    url = 'http://'+apisHosts['ventas']+'/ventas/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

def despachoApi():
    url = 'http://'+apisHosts['despacho']+'/despachos/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

"""
No poseo ruta exacta de post-venta

def post_ventaApi():
    url = 'http://'+apisHosts['post_venta']+'/post_venta/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

def contabilidadApi():
    url = 'http://'+apisHosts['contabilidad']+'/api/Facturas/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

"""
No poseo ruta exacta de stock

def stockApi():
    url = 'http://'+apisHosts['stock']+'/stock/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

"""
No poseo ruta exacta de seguridad

def seguridadApi():
    url = 'http://'+apisHosts['seguridad']+'/seguridad/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

def contarJson(json):
    filtered_data = [
        item for item in json 
        if 'datefield' in item and datetime.strptime(item['datefield'], '%Y-%m-%d').year == target_year
    ]
    return filtered_data