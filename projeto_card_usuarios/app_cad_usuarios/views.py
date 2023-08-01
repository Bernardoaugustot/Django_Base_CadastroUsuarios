from django.shortcuts import render

# Create your views here.
def home(request):
    #Request é um parametro do Django que puxa paradas de dentro da propria pagina.
    return render(request,'usuarios/home.html' )