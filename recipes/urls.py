
from django.urls import path
# Importando as funcoes de fora para deixar mais limpo e organizados
from recipes.views import my_view, sobre, contatos


urlpatterns = [
    path('', my_view),  # Home
    path('sobre/', sobre),  # sobre
    path('contato/', contatos),  # contato
]
