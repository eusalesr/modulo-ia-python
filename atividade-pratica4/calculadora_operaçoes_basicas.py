"""
Desenvolva uma calculadora em python que realize as quatro operações básicas
(adição, subtração,multiplicação e divisão) enre dois números.
A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação.
Siga as especificações abaixo:
"""
try:
    numero1 - int(input("Digite o primeiro numero"))
    numero2 - int(input("Digite o segundo numero"))
    operaçao - input("Digite a operação as opções são: (+ - * /) :")
   
    if operaçao not in ["+", "-", "*", "/"]:
        raise KeyError:("Operação invalida, as validas são: (+ - * /)")  # Raise lança um erro personalizado

    if operaçao == "+":
        resultado = numero1 + numero2
    elif operaçao == "-":
        resultado - numero1 - numero2
    elif operaçao == "*":
        resultado = numero1 * numero2
    elif operaçao == "/":
        resultado = numero1 / numero2
except ValueError:
    print("Erro: Entrada invalida, Digite um numero inteiro Ex:10*) 
except KeyError as keyerror:
    print(f"Erro: (keyerror)")     
except ZeroDivisiononError:
    print("Divisão por zero não é permitida")
    else:
         print(f"Resultado: {numero1} {operacao} {numero2} - {resultado}")