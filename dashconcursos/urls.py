from django.urls import path
from dashconcursos.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]