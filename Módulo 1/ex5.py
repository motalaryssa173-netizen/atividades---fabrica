numeros = []
impares = []
pares = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero) 

    else:
        impares.append(numero)

print(numeros)
print(pares)
print(impares)
