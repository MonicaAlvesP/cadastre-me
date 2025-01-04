from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

def home(request):
  return render(request, 'usuarios/home.html')

def usuarios(request):
  if request.method == 'POST':
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save() # Salva o novo usuário no banco de dados
  
  # Exibir todos os usuários cadastrados
  usuarios = {
    'usuarios': Usuario.objects.all()
  }
  
  return render(request, 'usuarios/usuarios.html', usuarios) # Passa a lista de usuários para o template

def remover_usuario(request, id):
  usuario = get_object_or_404(Usuario, id_usuario=id)
  usuario.delete() # Remove o usuário do banco de dados
  return redirect('usuarios') # Redireciona para a página de usuários