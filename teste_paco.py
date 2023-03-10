# Define a matriz de 20 x 10 com valores iguais a zero
matriz = [[0] * 10 for _ in range(20)]

# Define as peças
pecas = [
    [[1, 1], [1, 1], [1, 1], [1, 1]],  # peça 1
    [[2, 0], [2, 0], [2, 2], [0, 2]],  # peça 2
    [[0, 3], [3, 3], [3, 0], [0, 3]],  # peça 3
    [[4, 4, 4], [0, 4, 0], [0, 4, 0], [0, 0, 0]],  # peça 4
    [[0, 5, 5], [5, 5, 0], [0, 0, 0], [0, 0, 0]],  # peça 5
    [[0, 0, 0], [6, 6, 6], [0, 6, 0], [0, 0, 0]]   # peça 6
]

# Define a sequência de peças a serem encaixadas
sequencia = '65313243655652465636662646166324536256223665525256463525566534512662656666'

# Função que verifica se é possível encaixar a peça na posição (linha, coluna)
def pode_encaixar(peca, linha, coluna):
    for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != 0 and (linha + i >= 20 or coluna + j < 0 or coluna + j >= 10 or matriz[linha + i][coluna + j] != 0):
                return False
    return True

# Função que encaixa a peça na posição (linha, coluna)
def encaixar(peca, linha, coluna):
    for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != 0:
                matriz[linha + i][coluna + j] = peca[i][j]

# Percorre a sequência de peças e tenta encaixá-las na matriz
for p in sequencia:
    peca = pecas[int(p) - 1]
    encaixou = False
    for c in range(10):
        for l in range(20 - len(peca) + 1):
            if pode_encaixar(peca, l, c):
                encaixar(peca, l, c)
                encaixou = True
                break
        if encaixou:
            break
    if not encaixou:
        print(f'Não foi possível encaixar a peça {p} na matriz.')
        break

# Escreve a matriz resultante em um arquivo de texto
with open('resultado.txt', 'w') as f:
    for linha in matriz:
        f.write(' '.join(str(x) for x in linha) + '\n')
