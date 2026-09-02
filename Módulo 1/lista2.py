nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial:", nomes)

nomes.append("Carlos") #insere no final
print("Após append:", nomes)

nomes.insert(1, "Fernanda") #insere onde for informado
print("Após insert:", nomes)

nomes[2] = "Paulo"
print("Após modificado:", nomes)

del nomes [3] 
print("Após del:", nomes)

nomes.remove("Fernanda")
print("Após remove:", nomes)

removido = nomes.pop(2)
print(f"Após pop (removido '{removido}')", nomes)

nomes.clear()
print("Após clear:", nomes)