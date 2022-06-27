from django.urls import path #implementa path para criar rotas
from . import views # MVT model(armazena uma informação ) view(logica do projeto/manipular dados) e templates(mostra a manipulação)

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"), # para usuario
    path('plataforma/',views.plataforma,name='plataforma'),
    path('cadastro_livro/',views.cadastro_livro,name='cadastro_livro'),
] 