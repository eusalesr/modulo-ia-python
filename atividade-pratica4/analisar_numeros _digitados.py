# Função para verificar se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Função para analisar uma lista de números
def analisar_numeros(numeros):
    pares = 0
    impares = 0
    for num in numeros:
        if eh_par(num):
            pares += 1
        else:
            impares += 1
    return pares, impares

# Programa principal
def main():
    numeros = []
    qtd = int(input("Quantos números você quer digitar? "))
    
    for i in range(qtd):
        numero = int(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
    
    pares, impares = analisar_numeros(numeros)
    
    print(f"\nQuantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

if name == "main":
    main()