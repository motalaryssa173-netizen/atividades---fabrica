# Programa para calcular diferença entre preços em mercados diferntees

produto = input("Qual produto deseja consultar? ")
print(" "*50)
mercado1 = input("Qual o nome do primeiro mercado que deseja consultar? ")
print(" "*50)
preco_mercado1 = float(input("Digite o preço do produto no primeiro mercado: "))
print(" "*50)
mercado2 = input("Qual o nome do segundo mercado que deseja consultar? ")
print(" "*50)
preco_mercado2 = float(input("Digite o preço do produto no segundo mercado: "))
print(" "*50)
mercado3 = input("Qual o nome do terceiro mercado que deseja consultar? ")
print(" "*50)
preco_mercado3 = float(input("Digite o preço do produto no terceiro mercado: "))
print(" "*50)

if preco_mercado1 < preco_mercado2:
    print(f"=== Resultado ===\nProduto: {produto}\nMais barato em: {mercado1}\nPreço: {preco_mercado1:.2f}")

elif preco_mercado2 < preco_mercado3:
    print(f"=== Resultado ===\nProduto: {produto}\nMais barato em: {mercado2}\nPreço: {preco_mercado2:.2f}")

else:
    print(f"=== Resultado ===\nProduto: {produto}\nMais barato em: {mercado3}\nPreço: {preco_mercado3:.2f}")