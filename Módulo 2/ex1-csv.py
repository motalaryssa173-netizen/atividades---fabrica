import csv

with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade", "Nota"])

while True:
    menu = input("[1] Cadastrar aluno,nota e idade\n[2] Listar alunos\n[3] Listar alunos com nota acima de 8\n[0] Sair\n")

    if menu == "1":
        nome = input("Digite seu nome: ")
        nota = float(input("Digite sua nota: "))
        idade = int(input("Digite a sua idade: "))

        with open("dados.csv", "a", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome,idade,nota])

    elif menu == "2":
        with open("dados.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(f"{linha[0]} | {linha[1]} | {linha[2]}")
    
    elif menu == "3":
        with open("dados.csv", "r") as arquivo:
            leitor_csv = csv.reader(arquivo)

            next(leitor_csv)

            for linha in leitor_csv:
                if float(linha[2]) > 8:
                    print(f"{linha[0]} | {linha[1]} | {linha[2]}")
           
    elif menu == "0":
        break 

    else:
        print("Valor inválido")