# Função para verificar se a senha tem pelo menos 8 caracteres
def verifica_tamanho(senha):
    return len(senha) >= 8

# Função para verificar se a senha contém pelo menos um número
def verifica_numero(senha):
    return any(char.isdigit() for char in senha)

# Função principal para validar senha
def validar_senha(senha):
    if not verifica_tamanho(senha):
        return "Senha inválida! Deve ter pelo menos 8 caracteres."
    elif not verifica_numero(senha):
        return "Senha inválida! Deve conter pelo menos um número."
    else:
        return "Senha válida!"

# Programa principal
def main():
    senha = input("Digite uma senha para verificar: ")
    resultado = validar_senha(senha)
    print(resultado)

if name == "main":
    main()