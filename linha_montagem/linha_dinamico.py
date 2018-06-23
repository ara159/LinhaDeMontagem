from linha_montagem import argv

# Variável global para se calcular as instruções
contador = 0


def caminho_mais_rapido(estacoes, trocas, entrada, saida, n):
    # Inicializo as matrizes (Tabelas)
    custo = [[-1 for i in range(n)],
             [-1 for i in range(n)]]
    caminho = [[-1 for i in range(n)],
               [-1 for i in range(n)]]

    # Primeira estação [0]
    custo[0][0] = entrada[0]+estacoes[0][0]
    custo[1][0] = entrada[1]+estacoes[1][0]
    globals()["contador"] += 2

    # Segunda até n
    for j in range(1, n):
        # Para linha 1
        # Calculo vim da mesma linha e vim da outra linha
        vim_msm_linha = custo[0][j-1] + estacoes[0][j]
        vim_outra_linha = custo[1][j-1] + \
            trocas[1][j-1] + estacoes[0][j]

        # Comparo, qual é melhor? melhor = ter menor custo
        if vim_msm_linha <= vim_outra_linha:
            # Adiciono na tabela de custo o resultado encontrado
            custo[0][j] = vim_msm_linha
            # Adiciono na tabela de caminho o caminho correspondente
            caminho[0][j-1] = 0
        else:
            # Adiciono na tabela de custo o resultado encontrado
            custo[0][j] = vim_outra_linha
            # Adiciono na tabela de caminho o caminho correspondente
            caminho[0][j-1] = 1

        # Para linha 2
        # Calculo vim da mesma linha e vim da outra linha
        vim_msm_linha = custo[1][j-1] + estacoes[1][j]
        vim_outra_linha = custo[0][j-1] + \
            trocas[0][j-1] + estacoes[1][j]

        # Comparo, qual é melhor? melhor = ter menor custo
        if vim_msm_linha <= vim_outra_linha:
            # Adiciono na tabela de custo o resultado encontrado
            custo[1][j] = vim_msm_linha
            # Adiciono na tabela de caminho o caminho correspondente
            caminho[1][j-1] = 1
        else:
            # Adiciono na tabela de custo o resultado encontrado
            custo[1][j] = vim_outra_linha
            # Adiciono na tabela de caminho o caminho correspondente
            caminho[1][j-1] = 0

        if "--debug" in argv:
            print("=== ESTAÇÃO "+str(j)+" ===")
            print("Vetor Custo:", custo, "\nVetor Caminho:", caminho, "\n")

        globals()["contador"] += 4  # Quatro operações, 2 para cada linha

    globals()["contador"] += 2  # Saidas

    # Soma os valores de saída
    custo_final_l0 = custo[0][n-1] + saida[0]  # linha[0]
    custo_final_l1 = custo[1][n-1] + saida[1]  # linha[1]

    # Comparo, sair pela linha 0 é melhor que pela linha 1?
    if custo_final_l0 <= custo_final_l1:
        # Adiciono a tabela de caminho, que eu começo pela melhor linha
        caminho[0][n-1] = 0
        return custo_final_l0, caminho[0]
    else:
        # Adiciono a tabela de caminho, que eu começo pela melhor linha
        caminho[1][n-1] = 1
        return custo_final_l1, caminho[1]
