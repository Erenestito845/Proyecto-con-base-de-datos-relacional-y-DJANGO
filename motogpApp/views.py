from django.shortcuts import render

# Vista principal de MotoGP
def inicio(request):
    return render(request, 'motogp/inicio.html')

# Vista de la parrilla de pilotos
def pilotos(request):
    # Desconectamos la lectura del archivo 'motogp.json'
    # Enviamos una lista vacía para evitar que la página colapse
    context = {
        'pilotos': []  # Verifica si en tu plantilla usaste "pilotos" o "equipos"
    }
    # Asegúrate de que 'pilotos.html' sea el nombre correcto de tu archivo en la carpeta templates/motogp/
<<<<<<< HEAD
    return render(request, 'motogp/pilotos.html', context)
=======
    return render(request, 'motogp/pilotos.html', context)
>>>>>>> 4c35e3533d9847095ca28460a6a29fd5a95654b5
