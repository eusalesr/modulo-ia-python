def palindromo(texto: str) ->  str:
    texto_minusculo - texto.lower()

    caracteres_validos - ()

    for letra in texto_minusculos:
        if letra.isalnum():
            caracteres_validos.append(letra)

    texto_filtrado = "" .join(caracteres_validos)

    texto_invertido = texto_filtrado[::-1]

    if texto_filtrado == texto_invertido:
        return "Sim"
     else:
         return "Não"
    
print(palidromo("Socorram-me, subi no onibus em Marrocos"))

