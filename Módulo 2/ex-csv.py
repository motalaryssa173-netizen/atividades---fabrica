import csv 

with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"])
    escritor.writerow(["Ana", 9])
    escritor.writerow(["Maria", 7])
    escritor.writerow(["João", 8])

with open("dados.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)