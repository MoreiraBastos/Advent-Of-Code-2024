"""
Advent Of Code 2024
Problem 6
Edson Moreira Bastos
06/12/24
"""

# Inicializar a matriz
matriz = []

# Caminho do arquivo que contem a matriz
arquivo = "mapa.txt"

# Carregar a matriz do arquivo
with open(arquivo, "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        matriz.append(list(linha.strip()))  # Cada linha é uma lista de caracteres

# Verifica se a matriz é válida
if len(matriz) == 130 and all(len(coluna) == 130 for coluna in matriz):  # Ajustar conforme o tamanho da matriz de exemplo
    print("Matriz carregada corretamente.")

    # Encontrar o elemento inicial '^' na matriz
    posicao = None
    for i, linha in enumerate(matriz):
        if '^' in linha:
            posicao = (i, linha.index('^'))
            break

    if posicao:
        print(f"Elemento inicial '^' encontrado na posição: {posicao}")

        # Direções e seus deslocamentos
        direcoes = {
            '^': (-1, 0),  # Norte: decrementa linha
            'v': (1, 0),   # Sul: incrementa linha
            '>': (0, 1),   # Leste: incrementa coluna
            '<': (0, -1),  # Oeste: decrementa coluna
        }
        rotacao = ['^', '>', 'v', '<']  # Ordem para rodar à direita
        direcao_atual = '^'  # Direção inicial

        passos = 0  # Contador de passos
        visitadas = set()  # Conjunto de posições visitadas

        while True:
            i, j = posicao
            # Verifica se já visitou a posição, se sim, continua
            if (i, j) in visitadas:
              pass
            else: 
              visitadas.add((i, j))  # Marca a posição como visitada
              passos += 1

            # Calcula a próxima posição
            di, dj = direcoes[direcao_atual]
            nova_posicao = (i + di, j + dj)

            # Verifica se a nova posição está dentro dos limites
            ni, nj = nova_posicao
            if 0 <= ni < len(matriz) and 0 <= nj < len(matriz[0]):
                proxima_celula = matriz[ni][nj]

                # Se encontrar um obstáculo '#', roda 90º à direita
                if proxima_celula == '#':
                    direcao_atual = rotacao[(rotacao.index(direcao_atual) + 1) % 4]
                else:  # Movimento válido (inclui rastros e novas células)
                    posicao = nova_posicao
                    matriz[ni][nj] = direcao_atual  # Atualiza a direção na nova posição
            else:
                # Sai da matriz quando tentar mover para fora dela
                break

        # Exibe o total de posições distintas visitadas
        print(f"O jogador visitou {passos} posições distintas.")
        print(f"Posições distintas visitadas: {visitadas}")
else:
    print("Erro: A matriz não é 130x130.")
