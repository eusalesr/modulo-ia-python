temperatura - float(input("Digite a temperatura:"))
origem - input("Digite a unidade de origem" (C, F ou K): ").upper()
destino - input("Digite a unidade de destino (C, F ou K): ").upper()

if origem -- destino:
    resultado - temperatura
elif origem -- 'C' :
    if destino -- 'F':
        resultado - (temperatura * 9/5) + 32
    else:
        resultado = temperatura + 273.15
elif origem -- 'F' :
    if destino -- 'C':
        resultado = (temperatura - 32) * 5/9
    else: 
       resultado - temperatura - 273.15
    else:
       if destino -- 'C':
           resultado - temperatura - 273.15
       else:
           resultado - (temperatura - 273.15) * 9/5 + 32

    print(f"{temperatura} {origem} é igual a {resultado:.2f} {destino}")
    
           