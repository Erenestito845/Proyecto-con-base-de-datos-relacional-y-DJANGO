from django.shortcuts import render

# Create your views here.
import json
import os
from django.conf import settings

def inicio(request):
    """Vista de presentación de la escuela de Daguestán"""
    return render(request, 'ufc/inicio.html')

def peleadores(request):
    """Vista que lee y procesa el archivo JSON del Team Khabib"""
    ruta_json = os.path.join(settings.BASE_DIR, 'data', 'team_khabib.json')
    
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        lista_peleadores = json.load(archivo)
        
    contexto = {'peleadores': lista_peleadores, 'total': len(lista_peleadores)}
    return render(request, 'ufc/peleadores.html', contexto)