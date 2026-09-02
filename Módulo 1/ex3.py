notas = []

for i in range (4):
    nota = float(input(f"Digite a {i+1}° nota: "))
    notas.append(nota)
    
for nota in notas:
    print(nota)

media = sum(notas) / len(notas)
print(media)