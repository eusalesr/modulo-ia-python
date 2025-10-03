import requests

det buscar_endereço(cep):
url - f"https://viacep.com.br/ws/{cep}/json/"
resposta - requests.get(url)
resposta.raise_for_status()
dados - resposta.json()

if "erro" in dados:
    print("CEP não encontrado")
else:
    print(f"Rua: {dados["logradouro"]}")
    print(f"Bairro: {dados["bairro"]}")
    print(f"Cidade: {dados ["localidade"]}")
    print(f"Estado: {dados ["uf"]}")

 cep - input("Digite o CEP(somente numero):") 
 buscar_endereco(cep)
  