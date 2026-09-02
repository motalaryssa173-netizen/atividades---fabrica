num1 = float(input("Digite o primeiro número da sua operação: "))
num2 = float(input("Digite o segundo número da sua operação: "))

menu = input("[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n ")
try:
    if menu == "1":
        print(f"esultado: {num1+num2}")
    elif menu == "2":
        print(f"Resultado: {num1-num2}")
    elif menu == "3":
        print(f"Resultado: {num1*num2}")
    elif menu == "4":
        print(f"Resultado: {num1/num2}")
except:
    print("Não é possivel realizar a operação")


    