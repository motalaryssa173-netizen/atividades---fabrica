boi1 = input("Digite o nome do primeiro boi: ")
peso1 = float(input(f"Digite o peso do boi {boi1}: "))
boi2 = input("Digite o nome do segundo boi: ")
peso2 = float(input(f"Digite o peso do boi {boi2}: "))
boi3 = input("Digite o nome do terceiro boi: ")
peso3 = float(input(f"Digite o peso do boi {boi3}: "))

print("=== Ranking (mais pesado -> mais leve) ===")

if peso1 > peso2 and peso1 > peso3:
    if peso2 > peso3: 
        print(f"1) {boi1} - {peso1} kg\n2) {boi2} - {peso2} kg\n3) {boi3} - {peso3} kg")
    else:
        print(f"1) {boi1} - {peso1} kg\n2) {boi3} - {peso3} kg\n3) {boi2} - {peso2} kg")

elif peso2 > peso1 and peso2 > peso3:
    if peso1 > peso3:
        print(f"1) {boi2} - {peso2} kg\n2) {boi1} - {peso1} kg\n3) {boi3} - {peso3} kg")
    else: 
        print(f"1) {boi2} - {peso2} kg\n2) {boi1} - {peso1} kg\n3) {boi3} - {peso3} kg")

elif peso3 > peso2 and peso3 > peso2:
    if peso1 > peso2:
        print(f"1) {boi3} - {peso3} kg\n2) {boi1} - {peso1} kg\n3) {boi2} - {peso2} kg")
    else:
        print(f"1) {boi3} - {peso3} kg\n2) {boi2} - {peso2} kg\n3) {boi1} - {peso1} kg")
        
