from django.shortcuts import render

# Vista principal de UFC
def inicio(request):
    return render(request, 'ufc/inicio.html')

# Vista del roster/equipo
def peleadores(request):
    # Lista vacía temporal para evitar caídas
    context = {
        'equipo': [] 
    }
    return render(request, 'ufc/peleadores.html', context)