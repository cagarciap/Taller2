from django.shortcuts import render, HttpResponse
import requests
from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyB_0Gc1XK3BUwu8UKmaffIEH9tlkQvWKXI",
    'authDomain': "integradortaller3.firebaseapp.com",
    'databaseURL': "https://integradortaller3.firebaseio.com",
    'projectId': "integradortaller3",
    'storageBucket': "integradortaller3.appspot.com",
    'messagingSenderId': "490129345475",
    'appId': "1:490129345475:web:fda045bc53d76c273f8b76",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


diccionario ={}

def Inicio(request):
    return render(request, "calidad_aire/inicio.html")

def formularioAgregar(request):
    return render(request, "calidad_aire/formularioAgregar.html")

def visualizar(request):
    return render(request, "calidad_aire/visualizar.html")

def calidad_aire(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            codigo = request.GET.get('codigo')
            latitud = request.GET.get('latitud')
            longitud = request.GET.get('longitud')
            area = request.GET.get('area')
            producto = request.GET.get('producto')
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'PPM', 'value': value, 'codigo':codigo, 'latitud':latitud, 'longitud':longitud, 'area':area, 'producto':producto}
            database.child('prueba').push(args)
            response = requests.post('http://127.0.0.1:9000/reports/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:9000/reports/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "calidad_aire/calidad_aire.html", {'measures': measures})
