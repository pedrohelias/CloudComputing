import json
import requests
import time

chamada = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

chamada_conv = chamada.json()
cotacao_dolar = chamada_conv["USDBRL"]  

# print(cotacao_dolar)
while True:
	print("O Dolar está custando: R${} ".format(cotacao_dolar["bid"]))
	time.sleep(10)
