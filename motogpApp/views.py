from django.shortcuts import render

# Create your views here.
import json
import os
from django.conf import settings


def inicio(request):
  """Vista de presentación y bienvenida a la categoría de MotoGP"""
  return render(request, 'motogp/inicio.html')


def pilotos(request):
  """Vista funcional que lee y procesa el archivo JSON de pilotos"""
  ruta_json = os.path.join(settings.BASE_DIR, 'data', 'motogp.json')

  with open(ruta_json, 'r', encoding='utf-8') as archivo:
    lista_pilotos = json.load(archivo)

  # Pasamos los datos leídos a la plantilla a través del contexto
  contexto = {'pilotos': lista_pilotos, 'total_pilotos': len(lista_pilotos)}
  return render(request, 'motogp/pilotos.html', contexto)