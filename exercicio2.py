import random
random.seed(5)
contpar = 0
somapreto = 0
matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
maior = 0
colunamaior = 0
for i in range(0, 11):
    for j in range(0, 11):
        valor = random.randint(0, 9)
        if j == 3 and valor % 2 == 0 and valor != 0 and i + j < 11:
            contpar += 1
        matriz[i][j] = valor
        if i == 2 and valor > maior:
            maior = valor
            colunamaior = j
        if i + j < 11:
            somapreto+=valor

for i in range(0, 11):
    for j in range(0, 11):
        print(f"[{matriz[i][j]}]", end='')
    print()
print(f"\nO maior elemento da linha 2 contando a partir do 0 é o {maior} na coluna {colunamaior} (tambem contando a " f"partir do 0) ")
print(f"\nO percentual de elementos pares na coluna 3 (contando a partir do zero) é: {(contpar/9)*100:.2f}%")
print(f"\nA soma de todos os elementos da área hachurada da matriz é: {somapreto} ")
