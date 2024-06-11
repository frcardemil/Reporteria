from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return 'Saludos terricolas'

@app.get("/reporte")
def read_item():
    url1 = 'https://34.224.245.239:8000/reporteria/reporte'
    url2 = 'http://44.218.227.202:8000/reporteria/api/reporte/'
    r = requests.get(url2)
    json_data = r.json()
    return json_data