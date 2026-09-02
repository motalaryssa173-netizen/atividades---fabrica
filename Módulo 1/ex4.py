consoantes = []
letras = []
contadora = 0

for i in range (10):
   letra = input(f"Digite a {i+1}° letra: ").lower()
   letras.append(letra)

for letra in letras:
  if letra not in "aeiou":
    consoantes.append(letra)
    contadora += 1

print(consoantes)
print(contadora)