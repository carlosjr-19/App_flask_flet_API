import requests

BASE_URL = "http://127.0.0.1:5000"

def obtener_config_colores():
    return requests.get(f"{BASE_URL}/colores").json()

def obtener_config_formulario():
    return requests.get(f"{BASE_URL}/formulario").json()

def obtener_info_proceso():
    return requests.get(f"{BASE_URL}/info-proceso").json()