# Calculadora de consumo de combustível

# Dados da viagem
distancia_percorrida - int(input("Digite a distancia percorrida em km: "))
combustivel_gasto - int(input("Digite a quantidade gasta de combustivel em Litros"))

# Cálculo do consumo
consumo - distancia_percorrida / combustivel_gasto

# Exibição do resultado
print("\nDados da Viagem:")
print(f"Distancia Percorrida: {disancia_percorrida} Km")
print(f"Combustivel Gastos: {combustivel_gasto} Litros(s)")
print(f"Consumo Medio: {consumo:.2f} km/l")