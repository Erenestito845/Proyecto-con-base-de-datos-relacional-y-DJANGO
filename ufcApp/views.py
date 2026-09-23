from django.shortcuts import render

# Vista principal de UFC
def inicio(request):
    return render(request, 'ufc/inicio.html')

# Vista del roster/equipo
def peleadores(request):
    # En lugar de intentar abrir y leer 'team_khabib.json', 
    # enviamos una lista vacía a la plantilla temporalmente.
    # Aquí es exactamente donde inyectaremos el ORM de Django más adelante.
    context = {
        'equipo': []  # Si en tu plantilla usaste otro nombre de variable, cámbialo aquí.
    }
    return render(request, 'ufc/peleadores.html', context)

