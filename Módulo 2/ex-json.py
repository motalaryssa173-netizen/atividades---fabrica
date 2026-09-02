import json

alunos = [
    {
        "nome":"Ana", 
        "idade": 16,
        "nota": 9.0
    },
    {
        "nome": "Carlos",
        "idade": 17,
        "nota": 7.5,
    },
    {
        "nome": "Marina",
        "idade": 15,
        "nota": 8.8,
    }
]

print(alunos)
print(alunos[0])
print(alunos[0]["nome"])

for aluno in alunos:
    print(aluno["nome"], aluno["idade"], aluno["nota"])

with open("alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo, indent=4)

print("Dados salvos com sucesso!")

with open("alunos.json", "r") as arquivo:
    alunos = json.load(arquivo)

for aluno in alunos:
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Nota:", aluno["nota"])
    print("-" * 20)