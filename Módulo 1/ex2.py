numeros = [1,2,3,4,5,6,7,8,9,10]

for i in range(9, -1, -1):
    print(numeros [i])

numeros.clear()

for i in range(10):
    numero = float(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

contadora = 9
while contadora >= 0:
    print(numeros[contadora])
    contadora -= 1 

print (numeros[::-1])