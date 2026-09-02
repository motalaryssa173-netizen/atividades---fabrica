numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)

numeros.clear()

for i in range(5):
    numero = int(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

print(numeros)