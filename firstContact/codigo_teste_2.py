import json
import requests



chamada = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

chamada_conv = chamada.json()
cotacao_dolar = chamada_conv["USDBRL"]  # pegando apenas cotaçao do dolar

# print(cotacao_dolar)
print("O Dolar esta custando: R${} ".format(cotacao_dolar["bid"]))
