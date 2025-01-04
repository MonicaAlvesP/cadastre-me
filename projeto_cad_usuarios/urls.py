from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('remover_usuario/<int:id>/', views.remover_usuario, name='remover_usuario'),
]
