import requests
from datetime import datetime

#Reporteria
#44.218.227.202:8000   --Maikel-C
#34.224.245.239:8000   --Principal

#https://leckiam.github.io/prueba-aws/ es para las urls de los grupos que no poseo
#post_venta -- 44.220.241.211:8000 / https://leckiam.github.io/prueba-aws/post_venta.json 
#adquisiciones  -- 34.199.103.123:8000 / https://leckiam.github.io/prueba-aws/adquisiciones.json 
#despacho  -- 44.205.221.190:8000 / https://leckiam.github.io/prueba-aws/despacho.json 
#contabilidad -- 54.159.228.5:8000 / https://leckiam.github.io/prueba-aws/contabilidad.json 
apisHosts = {
    'adquisiciones' : '34.199.103.123:8000',
    'proveedor' : '0.0.0.0:8000',
    'ventas' : 'https://leckiam.github.io/prueba-aws/ventas.json',
    'despacho' : '44.205.221.190:8000',
    'post_venta' : 'https://leckiam.github.io/prueba-aws/post_venta.json',
    'contabilidad' : '54.159.228.5:8000',
    'stock' : 'https://leckiam.github.io/prueba-aws/stock.json',
    'reporteria' : '44.218.227.202:8000',
    'seguridad' : '0.0.0.0:8000',
}
var_fecha_areas = {
    'adquisiciones' : 'fecha_orden',
    'proveedor' : 'fecha_proveedor',
    'ventas' : 'fecha_venta',
    'despacho' : 'fecha_despacho',
    'post_venta' : 'fecha_solicitud',
    'contabilidad' : 'fecha_de_emicion',
    'stock' : 'fecha_actualizacion',
    'reporteria' : 'anno_mes_rt',
}

def JSON_filtro(json,name,anno,mes):
    name_var_fecha=var_fecha_areas[name]
    json_filtrado = [
        item for item in json 
        if item[name_var_fecha][:4] == str(anno) and 
            item[name_var_fecha][5:7] == mes
    ]
    return json_filtrado

def reporteriaApi():
    url = 'http://'+apisHosts['reporteria']+'/reporteria/api/reporte/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

def adquisicionesApi(anno,mes):
    try:
        url = 'http://'+apisHosts['adquisiciones']+'/api/v1/productos/'
        r = requests.get(url)
    except:
        #url = apisHosts['adquisiciones']
        url = 'https://leckiam.github.io/prueba-aws/adquisiciones.json'
        r = requests.get(url)
    if r.status_code == 200:
        json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'adquisiciones',anno,mes)
    else:
        json_filtrado = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return json_filtrado

"""
No poseo ruta exacta de proveedor

def proveedorApi():
    url = 'http://'+apisHosts['proveedor']+'/proveedor/'
    r = requests.get(url)
    json_data = r.json(anno,mes)
    json_filtrado = JSON_filtro(json_data,'proveedor',anno,mes)
    return json_filtrado
"""

def ventasApi(anno,mes):
    #url = 'http://'+apisHosts['ventas']+'/ventas/'
    url = apisHosts['ventas']
    r = requests.get(url)
    if r.status_code == 200:
        json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'ventas',anno,mes)
    else:
        json_filtrado = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return json_filtrado

def despachoApi(anno,mes):
    try:
        url = 'http://'+apisHosts['despacho']+'/despachos/'
        r = requests.get(url)
    except:
        #url = apisHosts['despacho']
        url = 'https://leckiam.github.io/prueba-aws/despacho.json'
        r = requests.get(url)
    if r.status_code == 200:
        json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'despacho',anno,mes)
        
        despachos_intentos = [
            item for item in json_filtrado 
            if item['intento'] == 1
        ]
    else:
        json_filtrado = [1]
        despachos_intentos = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return [json_filtrado,despachos_intentos]

def post_ventaApi(anno,mes):
    #url = 'http://'+apisHosts['post_venta']+'/post_venta/'
    url = apisHosts['post_venta']
    r = requests.get(url)
    if r.status_code == 200:
        json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'post_venta',anno,mes)
    else:
        json_filtrado = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return json_filtrado

def contabilidadApi(anno,mes):
    try:
        url = 'http://'+apisHosts['contabilidad']+'/api/Facturas/'
        r = requests.get(url)
    except:
        #url = apisHosts['contabilidad']
        url = 'https://leckiam.github.io/prueba-aws/contabilidad.json'
        r = requests.get(url)
    if r.status_code == 200:
        json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'contabilidad',anno,mes)
        facturas_pagadas = [
            item for item in json_filtrado 
            if item['Estado_de_la_factua'] == 1
        ]
    else:
        json_filtrado = [1]
        facturas_pagadas = 1
        print(f'Error en la petición GET: {r.status_code}')
        
    return [json_filtrado,facturas_pagadas]


def stockApi(anno,mes):
    #url = 'http://'+apisHosts['stock']+'/stock/'
    url = apisHosts['stock']
    r = requests.get(url)
    if r.status_code == 200:
        json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'stock',anno,mes)
        
        suma_cantidades = 0
        for obj in json_filtrado:
            suma_cantidades += obj.get('cantidad', 0)
    else:
        json_filtrado = [1]
        suma_cantidades = 1
        print(f'Error en la petición GET: {r.status_code}')
        
    return [json_filtrado,suma_cantidades]

"""
No poseo ruta exacta de seguridad

def seguridadApi():
    url = 'http://'+apisHosts['seguridad']+'/seguridad/'
    r = requests.get(url)
    json_data = r.json()
    return json_data
"""


def obtenerRG(anno,mes):
    reporte_General= {
        'entrega_total':len(despachoApi(anno,mes)[0]),
        'entrega_a_tiempo':len(despachoApi(anno,mes)[1]),
        'stock_productos':stockApi(anno,mes)[1],
        'pedido_proveedor':1,
        'adquisicion_recibida':len(adquisicionesApi(anno,mes)),
        'venta_pedido':len(post_ventaApi(anno,mes)),
        'venta_realizada':len(ventasApi(anno,mes)),
        'factura_total':len(contabilidadApi(anno,mes)[0]),
        'factura_pagada':len(contabilidadApi(anno,mes)[1])
    }
    print(reporte_General)
    return reporte_General
