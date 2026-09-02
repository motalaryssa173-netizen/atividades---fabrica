with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, isso foi gerado automaticamente!")