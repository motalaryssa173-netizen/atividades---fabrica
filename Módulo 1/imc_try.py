peso = float(input("Digite seu peso: "))
altura =float(input("Digite sua altura (em cm): "))
imc = peso / (altura * altura)

try:
    imc <= 29.9
    print("Tudo certo!")
except:
    print("Melhore!")
