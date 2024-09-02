
from django.urls import path
# Importando as funcoes de fora para deixar mais limpo e organizados
from recipes.views import my_view


urlpatterns = [
    path('', my_view),  # Home
    path('home/', my_view),  # Home
]
