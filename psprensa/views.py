from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from django.db import connection


from .models import TabelaBin

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

import re
print(connection.queries)


def infoTableBINs(BIN,dado_sensivel_client_ID):
  informacoesHTTP=RequestsHTTPTransport(
      url='https://hml-api.elo.com.br/graphql',
      use_json=True,
      headers={
          "Content-type": "application/json",
          "client_id": dado_sensivel_client_ID 
      },
  )

  cliente = Client(transport=informacoesHTTP, fetch_schema_from_transport=True)

  consulta = gql("query OneBin { bin(number: \" "+ str(BIN)+" \") {  issuer {  name } product { name } allowedCaptures { name  code } usages {  name  code  }  services {  name  isExchangeableOffer }}}")

  return cliente.execute(consulta)




def index(request):
     return render(request,'viewsPrensa/index.html')

@csrf_protect
def consulta_bin(request):
    numerobin=""
    retorno = " "
    if(request.method =="POST"):
        numerobin = request.POST["codigobin"]
        if(numerobin.isnumeric()):
            if(len(numerobin) == 6):
                retorno = infoTableBINs(numerobin, "d92b1009-8940-34cc-ae28-5b1dabea9d29")
            else:
                retorno = "Erro de Validação: Digite um código que contenha apenas 6 digítos númericos!"
        else:
            retorno = "Erro de Digitação: Digite apenas números!"
    print(retorno)
       
    return render(request,'viewsPrensa/index.html',{'mensagemRetorno': retorno})



"""
O Erro ocorreu dentro do banco de dados consulta_bin depois quando eu o atualizei 
      print(numerobin)
            query = TabelaBin.objects.get(number_bin=numerobin)
            if query:
                #Imprime os dados
            else:
            #busca na api
                if(numerobin.isnumeric()):
                    if(len(numerobin) == 6):
                        retorno = infoTableBINs(numerobin)
                        #adiciona o número a tabela
                        dados = TabelaBin(
                            number_bin = ,
                            name_issuer = ,
                            name_product = ,
                            allowedCaptures_name = ,
                            allowedCaptures_code = ,
                            usages_name = ,
                            usages_code = ,
                            services_name = ,
                            services_isExchangeableOffer = 
                            )
                    else:
                        retorno = "Erro de Validação: Digite um código que contenha apenas 6 digítos númericos!"
                else:
                    retorno = "Erro de Digitação: Digite apenas números!"    
 
"""    