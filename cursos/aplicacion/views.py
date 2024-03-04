from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'aplicacion/index.html')

def cursos(request):
    return render(request, 'aplicacion/cursos.html')

def profesores(request):
    return render(request, 'aplicacion/profesores.html')

def estudiantes(request):
    return render(request, 'aplicacion/estudiantes.html')

def entregables(request):
    return render(request, 'aplicacion/entregables.html')
