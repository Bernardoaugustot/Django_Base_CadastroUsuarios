from django.shortcuts import render
from .models import Usuario
# Create your views here.
def home(request):
    #Request é um parametro do Django que puxa paradas de dentro da propria pagina.
    return render(request,'usuarios/home.html' )

#usuarios
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os usuarios Já cadastrados em uma nova página.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return  render(request, 'usuarios/usuarios.html', usuarios)