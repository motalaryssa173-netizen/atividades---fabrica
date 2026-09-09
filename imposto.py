def somarImposto(valor,taxa):
    return valor + (valor * taxa / 100)

valor = float(input("Digite o valor do produto: "))
taxa = float(input("Digite o valor da taxa: "))

valorImposto = somarImposto(valor,taxa)
print(f"Preço final com imposto: R${valorImposto}")