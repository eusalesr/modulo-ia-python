from datetime import date

# Função que recebe data de nascimento(inteiro) e retorna a conversao da idade em dias(inteiro)
def idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = date.today().year
    idade_anos = ano_atual - ano ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

resultado - idade_em_dias(1995)
print(f"A sua idade convertida é {resultado} dias")

