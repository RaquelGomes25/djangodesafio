from django.shortcuts import render, redirect
from .models import Livro
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    livros = Livro.objects.all() #pega tudo o que foi cadastrado no nosso model Livro
    return render(request, 'home.html', {'livro': livros}) 

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
            
        user = authenticate(username=username,password=senha)
        if(user):
            login_django(request, user)
            return HttpResponse('Logado no Sistema') 
        else:
            return HttpResponse('Usuário ou Senha inválidos')
        
def cadastro_livro(request):
    if request.method == "GET":
        return render(request, 'cadastro_livro.html')
    else:
        titulo = request.POST.get('titulo') 
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        data_cadastro = request.POST.get('data_cadastro')
                    
        livro = Livro.objects.filter(titulo=titulo).first() 
        
        if livro:
            return HttpResponse('Esse livro já está cadastrado.')
        livro = Livro.objects.create(titulo=titulo, autor=autor, editora=editora, data_cadastro=data_cadastro)
        livro.save()
        return redirect('/livros')        

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username') 
        email = request.POST.get('email')
        senha = request.POST.get('senha')
                    
        user = User.objects.filter(username=username).first() 
        
        if user:
            return HttpResponse('Já existe esse usuário cadastrado.')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuário cadastrado com Sucesso.')
    
def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse('Autenticado') #Só vai puder acessar quem estiver logado
    return HttpResponse('Você precisa estar logado')

