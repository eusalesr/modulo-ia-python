import requests

def consultar_cotacao(moeda)
    url - f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json(

    chave - moeda + "BRL"
    it chave not in dados:
        print("Moeda não encontrada")
        return

info - dados[chave]
print(f"Cotação {moeda}/BRL")
print(f"Valor Atual: {info["bid"]}")
print(f"Valor Maximo: {info["high"]}")
print(f"Valor Minimo: {info["low"]}")
print(f"Ultima Atualização: {info["create_date"]}")

moeda = input("Digite o codigo da moeda (Wx: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda)