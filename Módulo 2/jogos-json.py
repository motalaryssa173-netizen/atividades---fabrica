import json

jogos = None

while True:
    menu = input("[1] - Cadastrar\n[2] - Listar jogos\n[3] - Exibir notas\n[4] - Remover jogo\n[0] - Sair\n")

    if menu == "1":
        nome = input("Digite o nome do jogo: ")
        genero = input("Digite o gênero do jogo: ")
        nota = float(input("Digite a nota do jogo: "))
        plataforma = input("Digite a plataforma do jogo: ")

        jogo = {
            "nome" : nome,
            "genero" : genero,
            "nota" : nota,
            "plataforma" : plataforma
        }

        try:
            with open("jogos.json", "r") as arquivo:
                jogos = json.load(arquivo)
        except:
            print("Arquivo não encontrado.")
        finally:
            if jogos is not None:
                jogos.append(jogo)
            else:
                jogos = []
                jogos.append(jogo)
            with open("jogos.json", "w") as arquivo:
                json.dump(jogo, arquivo, indent=4)

    elif menu == "2":
        try:
            with open("jogos.json", "r") as arquivo:
                jogos = json.load(arquivo)

            for jogo in jogos:
                print(jogo["nome"])
                print(jogo["genero"])
                print(jogo["nota"])
                print(jogo["plataforma"])
                print("-" *20)
        except:
            print("Arquivo não encontrado.")

    elif menu == "3":
        float(print(jogo["nota"]))

    elif menu == "4":
        with open("jogos.json", "r") as arquivo:
            jogos = json.load(arquivo)
            jogos.remove("nome")
            print(f"Após removido:{jogo}")
                  
    elif menu == "0":
        break

    else:
        print("Valor inválido.")