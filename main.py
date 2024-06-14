from fastapi import FastAPI
import requests

apisHosts = {
    'adquisiciones' : '34.199.103.123:8000',
    'proveedor' : '0.0.0.0:8000',
    'ventas' : '0.0.0.0:8000',
    'despacho' : '44.205.221.190:8000',
    'post_venta' : '44.220.241.211:8000',
    'contabilidad' : '54.159.228.5:8000',
    'stock' : '0.0.0.0:8000',
    'reporteria' : '34.224.245.239:8000',
    'seguridad' : '0.0.0.0:8000',
}

app = FastAPI()

@app.get("/")
def read_root():
    return 'Saludos terricolas'

@app.get("/reportedespachos")
def read_item():
    url = 'http://'+apisHosts['reporteria']+'/reporteria/api/reportesdespachos/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

@app.get("/reporte")
def read_item():
    url = 'http://44.218.227.202:8000/reporteria/api/reporte/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

@app.get("/adquisiciones")
def read_item():
    url = 'http://'+apisHosts['adquisiciones']+'/api/v1/productos/'
    r = requests.get(url)
    json_data = r.json()
    return json_data


"""
No poseo ruta exacta de proveedor

@app.get("/proveedor")
def read_item():
    url = 'http://'+apisHosts['proveedor']+'/proveedor/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""


"""
No poseo ruta exacta de ventas

@app.get("/ventas")
def read_item():
    url = 'http://'+apisHosts['ventas']+'/ventas/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

@app.get("/despacho")
def read_item():
    url = 'http://'+apisHosts['despacho']+'/despachos/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

"""
No poseo ruta exacta de post-venta

@app.get("/post_venta")
def read_item():
    url = 'http://'+apisHosts['post_venta']+'/post_venta/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

@app.get("/contabilidad")
def read_item():
    url = 'http://'+apisHosts['contabilidad']+'/api/Facturas/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

"""
No poseo ruta exacta de stock

@app.get("/stock")
def read_item():
    url = 'http://'+apisHosts['stock']+'/stock/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""

"""
No poseo ruta exacta de seguridad

@app.get("/seguridad")
def read_item():
    url = 'http://'+apisHosts['seguridad']+'/seguridad/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""