pop_a = 80000
pop_b = 200000
taxa_a = 3
taxa_b = 1.5
ano = 0

while True:
    pop_a = pop_a + (pop_a * taxa_a / 100)
    pop_b = pop_b + (pop_b * taxa_b / 100)
    ano += 1

    if pop_a >= pop_b:
        print(f"Após {ano} anos, A alcança/ultrapassa B.\nPopulação final estimada:\n- País A: {pop_a} habitantes\n- País B: {pop_b} habitantes")
        break