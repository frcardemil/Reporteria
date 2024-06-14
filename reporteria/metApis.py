import requests

def requestApis(area):
    url='https://172.31.20.240:8000/'+area
    r = requests.get(url)
    print(r.status_code)
    if r.status_code == 200:
        print('viva xd')
        return r.json()
    else:
        print('no viva :c')
        return []

def contarTotal(json):
    total = 0
    return total

def listarDatosDash():
    lista =[]
    return lista
