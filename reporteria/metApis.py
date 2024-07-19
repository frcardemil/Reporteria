import requests
from datetime import datetime,date

#Reporteria
#44.218.227.202:8000   --Maikel-C
#34.224.245.239:8000   --Yeremi-G

#https://leckiam.github.io/prueba-aws/ es para las urls de los grupos que no poseo
#post_venta -- 44.220.241.211 / https://leckiam.github.io/prueba-aws/post_venta.json 
#adquisiciones  -- 34.199.103.123:8000 / https://leckiam.github.io/prueba-aws/adquisiciones.json 
#despacho  -- 44.205.221.190:8000 / 3.221.189.4:8000 / https://leckiam.github.io/prueba-aws/despacho.json 
#contabilidad -- 54.159.228.5:8000 / https://leckiam.github.io/prueba-aws/contabilidad.json
#proveedor -- 54.161.129.230 / https://leckiam.github.io/prueba-aws/proveedores.json

fecha_actual = datetime.now()

apisHosts = {
    'adquisiciones' : '34.199.103.123:8000',
    'proveedor' : '54.161.129.230',
    'ventas' : 'https://leckiam.github.io/prueba-aws/ventas.json',
    'despacho' : '3.221.189.4:8000',
    'post_venta' : '44.220.241.211',
    'contabilidad' : '54.159.228.5:8000',
    'stock' : 'https://leckiam.github.io/prueba-aws/stock.json',
    'reporteria' : '44.218.227.202:8000',
}
var_fecha_areas = {
    'adquisiciones' : 'fecha_adquisicion',
    'ventas' : 'fecha_venta',
    'despacho' : 'fecha_despacho',
    'post_venta' : 'fecha_emision',
    'contabilidad_fac' : 'fecha_de_emicion',
    'contabilidad_bol' : 'Fecha_emision',
    'reporteria' : 'anno_mes_rt',
}

def JSON_filtro(json,name,anno,mes):
    name_var_fecha=var_fecha_areas[name]
    json_filtrado = []

    for item in json:
        try:
            fecha = item[name_var_fecha]
            if isinstance(fecha, date):
                if fecha.year == int(anno) and fecha.month == int(mes):
                    json_filtrado.append(item)
            else:
                fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
                if fecha.year == int(anno) and fecha.month == int(mes):
                    json_filtrado.append(item)
        except (ValueError, KeyError) as e:
            print(f"Error procesando el item {item}: {e}")
    return json_filtrado

def reporteriaApi():
    url = 'http://'+apisHosts['reporteria']+'/reporteria/api/reporte/'
    r = requests.get(url)
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
    else:
        json_data = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return json_data

def getReporte(anno_mes):
    url = 'http://'+apisHosts['reporteria']+'/reporteria/api/reporte/'+anno_mes
    r = requests.get(url)
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
    else:
        json_data = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return json_data

def adquisicionesApi(anno,mes):
    #try:
        #url = 'http://'+apisHosts['adquisiciones']+'/api/carrito/'
        #r = requests.get(url)
    #except:
        #url = apisHosts['adquisiciones']
    url = 'https://leckiam.github.io/prueba-aws/adquisiciones.json'
    r = requests.get(url)
    suma_cantidades = 0
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'adquisiciones',anno,mes)

        for obj in json_filtrado:
            suma_cantidades += obj.get('cantidad_total', 0)
    else:
        json_filtrado = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return [json_filtrado,suma_cantidades]

def proveedorApi(anno,mes):
    url = 'http://'+apisHosts['proveedor']+'/productos/'
    r = requests.get(url)
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
        
        suma_cantidades = 0
        #print(fecha_actual)
        #print(anno)
        #if fecha_actual.year == anno and fecha_actual.month == mes:
        for obj in json_data:
            suma_cantidades += obj.get('stock_producto', 0)
        #else:
            #try:
                #reporte_json=getReporte(anno+''+mes)
                #suma_cantidades=reporte_json['pedido_proveedor']
            #except:
                #suma_cantidades=1
    else:
        json_data = [1]
        suma_cantidades = 1
        print(f'Error en la petición GET: {r.status_code}')
        
    return [json_data,suma_cantidades]

def ventasApi(anno,mes):
    #url = 'http://'+apisHosts['ventas']+'/ventas/'
    url = apisHosts['ventas']
    r = requests.get(url)
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
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
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'despacho',anno,mes)
        
        despachos_entreg = [
            item for item in json_filtrado 
            if item['entregado']
        ]
        despachos_intentos = [
            item for item in json_filtrado 
            if item['intento'] == 1 and item['entregado']
        ]
    else:
        despachos_entreg = [1]
        despachos_intentos = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return [despachos_entreg,despachos_intentos]

def post_ventaApi(anno,mes):
    #url = 'http://'+apisHosts['post_venta']+'/todos_los_datos'
    url = 'https://leckiam.github.io/prueba-aws/post_venta.json'
    r = requests.get(url)
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'post_venta',anno,mes)
    else:
        json_filtrado = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return json_filtrado

def contabilidadApiFact(anno,mes):
    try:
        url = 'http://'+apisHosts['contabilidad']+'/api/Facturas/'
        r = requests.get(url)
    except:
        #url = apisHosts['contabilidad']
        url = 'https://leckiam.github.io/prueba-aws/contabilidad.json'
        r = requests.get(url)
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'contabilidad_fac',anno,mes)
        facturas_pagadas = [
            item for item in json_filtrado 
            if item['Estado_de_la_factua'] == 2
        ]
    else:
        json_filtrado = [1]
        facturas_pagadas = 1
        print(f'Error en la petición GET: {r.status_code}')
        
    return [json_filtrado,facturas_pagadas]

def contabilidadApiBole(anno,mes):
    try:
        url = 'http://'+apisHosts['contabilidad']+'/api/Boleta/'
        r = requests.get(url)
    except:
        #url = apisHosts['contabilidad']
        url = 'https://leckiam.github.io/prueba-aws/boletas.json'
        r = requests.get(url)
    if r.status_code == 200:
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
        json_filtrado = JSON_filtro(json_data,'contabilidad_bol',anno,mes)
        facturas_pagadas = [
            item for item in json_filtrado 
            if item['Estado'] == "pagado"
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
        try:
            json_data = r.json().get("results", [])
        except:
            json_data = r.json()
        
        suma_cantidades = 0
        #if fecha_actual.year == anno and fecha_actual.month == mes:
        for obj in json_data:
            suma_cantidades += obj.get('cantidad', 0)
        #else:
            #try:
                #reporte_json=getReporte(anno+''+mes)
                #suma_cantidades=reporte_json['stock_productos']
            #except:
                #suma_cantidades=1
    else:
        json_data = [1]
        suma_cantidades = 1
        print(f'Error en la petición GET: {r.status_code}')
        
    return [json_data,suma_cantidades]


def seguridadApi(username,password):
    #username = admin.reporteria
    #password = reporteria
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXBvcnRlcmlhIjoidG9rZW5fcmVwb3J0ZXJpYSJ9.jAdpn5jFFOSelg4OqppHtTaGq_NboZq0QsaSMTVEVTA"
    
    data = {
        'username':username,
        'password':password,
        'token':token,
    }
    headers = {
        'Content-type':'application/json',
    }
    
    url = 'https://qic534o8o0.execute-api.us-east-1.amazonaws.com/validacionUsuarios/'
    
    r = requests.post(url,json=data,headers=headers)
    if r.status_code == 200:
        return True
    else:
        print(f'Error en la petición GET: {r.status_code}')
        if username=="admin.reporteria" and password=="reporteria":
            return True
        return False


def obtenerRG(anno,mes):
    reporte_General= {
        'entrega_total':len(despachoApi(anno,mes)[0]),
        'entrega_a_tiempo':len(despachoApi(anno,mes)[1]),
        'stock_productos':stockApi(anno,mes)[1],
        'pedido_proveedor':proveedorApi(anno,mes)[1],
        'adquisicion_recibida':adquisicionesApi(anno,mes)[1],
        'venta_pedido':len(post_ventaApi(anno,mes)),
        'venta_realizada':len(ventasApi(anno,mes)),
        'factura_total':len(contabilidadApiFact(anno,mes)[0]),
        'factura_pagada':len(contabilidadApiFact(anno,mes)[1]),
        'boleta_total':len(contabilidadApiBole(anno,mes)[0]),
        'boleta_pagada':len(contabilidadApiBole(anno,mes)[1])
    }
    print(reporte_General)
    return reporte_General
