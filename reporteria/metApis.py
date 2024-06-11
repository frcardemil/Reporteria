import requests
apisHosts = {
    'adquisiciones' : ['34.199.103.123','/'],
    'proveedor' : ['0.0.0.0','/'],
    'ventas' : ['0.0.0.0','/'],
    'despacho' : ['44.205.221.190','/'],
    'post_venta' : ['44.220.241.211','/'],
    'contabilidad' : ['54.159.228.5','/'],
    'stock' : ['0.0.0.0','/'],
    'reporteria' : ['34.224.245.239','/'],
    'seguridad' : ['0.0.0.0','/'],
}

def requestApis(user,password,area,modelo):
    url='https://'+apisHosts[area]+':8000'+modelo
    r = requests.get(url, auth=(user, password))
    print(r.status_code)
    if r.status_code == 200:
        return r.json()
    else:
        return []

def contarTotal(json):
    total = 0
    return total

def listarDatosDash():
    lista =[]
    return lista
