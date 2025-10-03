# Função para cadastrar alunos e suas notas
def cadastrar_alunos():
    alunos = []
    qtd_alunos = int(input("Digite a quantidade de alunos: "))

    for i in range(qtd_alunos):
        nome = input(f"\nDigite o nome do aluno {i+1}: ")
        notas = []
        for j in range(3):  # 3 notas por aluno
            nota = float(input(f"Digite a nota {j+1} de {nome}: "))
            notas.append(nota)

        media = calcular_media(notas)
        alunos.append({"nome": nome, "notas": notas, "media": media})
    return alunos

# Função para calcular média a partir de uma lista de notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para exibir resultados dos alunos
def exibir_resultados(alunos):
    print("\n--- Resultados ---")
    soma_medias = 0
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}\n")
        soma_medias += aluno['media']
    
    media_turma = calcular_media([aluno['media'] for aluno in alunos])
    print(f"Média da turma: {media_turma:.2f}")

# Programa principal
def main():
    alunos = cadastrar_alunos()
    exibir_resultados(alunos)

# Executa o programa
if name == "main":
    main()