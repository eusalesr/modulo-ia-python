peso - float(input("Digite seu peso kg:"))
altura - float(input("Digite sua altura em metros:"))

imc  - peso / (altura ** 2)

if imc < 18.5:
    classificaçao - "Abaixo do Peso"
elif imc > 18.5 and imc <- 25:
    classificaçao - "Peso normal"
elif imc > 25 and imc <= 30:
    classificaçao = "Sobrepeso"
else:
    classificado - "Obeso"

print(f"Seu IMC: {imc: .1f}")
print(f"Classificação: {classificaçao}")
