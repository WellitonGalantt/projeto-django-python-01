
# #* O render serve para podermos renderizar templates como html na pagina
from django.shortcuts import render
from django.http import HttpResponse


# #*HTTP request(Um pedido para o servidor)
# #*HTTP response(Uma resposta do servidor);
def my_view(req):
    # #*Passamos uma requisisao e o caminho do template;
    # #*Criando uma pasta com nome templates
    # #*ele ja busca automaticamento o arquivo como nome passado
    return render(req, 'recipes/home.html', context={
        'name': 'Welliton'
    })


def sobre(req):
    return HttpResponse('Pagina sobre')


def contatos(req):
    return HttpResponse('Pagina contatos')
