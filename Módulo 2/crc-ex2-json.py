import json

produtos = None

while True:
    menu = input("[1] - Cadastro de produtos\n[2] - Listar produtos\n[3] - Consultar preços\n[0] - Sair\n")

    if menu == "1":
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        quantidade_estoque = input("Digite a quantidade de produtos em estoque: ")
        preco_produto = input("Digite o preço desse produto: ")

        produto = {
            "produto" : nome,
            "categoria" : categoria,
            "quantidade_estoque" : quantidade_estoque,
            "preco_produto" : preco_produto
        }

        try:
            with open("mercado.json", "r") as arquivo:
                produtos = json.load(arquivo)
        except:
            print("Arquivo não encontrado.")
        finally:
            if produtos is not None:
                produtos.append(produto)
            else:
                produtos = []
                produtos.append(produto)
            with open("mercado.json", "w") as arquivo:
                json.dump(produtos, arquivo, indent=4)
    
    elif menu == "2":
        try:
            with open("mercado.json", "r") as arquivo:
                produtos = json.load(arquivo)

            for produto in produtos:
                print(produto["produto"])
                print(produto["categoria"])
                print(produto["quantidade_estoque"])
                print(produto["preco_produto"])
                print("-" *20)

        except:
            print("Arquivo não encontrado.")

    elif menu == "3":
        preco = float(input("Digite o preço consultado: "))
        try:
            with open("mercado.json", "r") as arquivo:
                produtos = json.load(arquivo)

            for produto in produtos:
                if float(produto[preco]) >= preco:
                    print(produto["produto"])
                    print(produto["categoria"])
                    print(produto["quantidade_estoque"])
                    print(produto["preco_produto"])
                    print("-" *20)
        except:
            print("Arquivo não encontrado.")

    elif menu == "0":
        break

    else:
        print("Opção inválida!")
