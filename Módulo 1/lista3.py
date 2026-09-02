#meu código
while True:
    cadastrar = [(input("Digite o nome da pessoa para o cadastro:"))]
    listar = [cadastrar]
    print("Lista atual:", listar)

    remover = (input("Digite o nome que deseja remover:"))
    cadastrar.remove(remover)
    print("Após removido:", listar)
    break 

#correção do professor

agenda = []
while True:
    menu = input("[1] Cadastrar pessoas\n[2] Listar pessoas\n[3] Excluir pessoa\n[0] Sair ")

    if menu == "1":
        nome = input("Digite o nome: ")
        agenda.append(nome)
    elif menu == "2":
        print(agenda)
        for nome in agenda:
            print(nome)
    elif menu == "3":
        nome = input("Digite o nome: ")
        agenda.remove(nome)
    elif menu == "0":
        break
    else:
        print("Valor inválido.")

