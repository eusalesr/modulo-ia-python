import requests

det obter_usuario_aleatorio():
    url - "https://randomuser.me/api/"
    resposta - requests.get(url)
    resposta.raise_for_status()
    dados - respostas.json()

    usuario = dados["resultado"][0]
    nome = usuario["name"]["first"] + "" + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")

obter_usuario_aleatorio()

   
    