from random import randint
from sys import argv

# Variável global para contar as instruções
contador = 0


def caminho_mais_rapido(estacoes, trocas, entradas, lin_at, est_at, caminho):
    globals()["contador"] += 1  # Adiciona 1 ao custo para cada recurssão
    if "--debug" in argv:
        print("=== ESTAÇÃO "+str(est_at)+" ===")
        print("Vetor Custo:", estacoes, "\nVetor Caminho:", caminho, "\n")

    # Ponto de parada, est_at == 0
    if est_at == 0:
        # Paro quando estou na estação 0, pois não preciso mais recorrer para
        # calcular o melhor caminho só existe 1
        return entradas[lin_at]+estacoes[lin_at][0]

    # est_at > 0
    # Caso seja a linha 0
    if lin_at == 0:
        # Recorro ao anterior da MESMA linha (linha=0, est_at=est_at-1)
        vim_msm_linha = caminho_mais_rapido(
            estacoes, trocas, entradas, 0, est_at-1, caminho)
        vim_msm_linha += estacoes[0][est_at]
        # Recorro ao anterior da OUTRA linha (linha=1, est_at=est_at-1)
        # aqui tem que considerar o custo de transferir de linha
        vim_outra_linha = caminho_mais_rapido(
            estacoes, trocas, entradas, 1, est_at-1, caminho)
        vim_outra_linha += estacoes[0][est_at] + trocas[1][est_at-1]
        # Pergunto, vim da msm linha é melhor? (melhor=menor custo)
        if vim_msm_linha <= vim_outra_linha:
            # Para linha atual (0), é melhor permanecer (0),
            # ou seja, passei pela linha 0 na estação est_at anterior
            caminho[0][est_at-1] = 0
            return vim_msm_linha
        else:
            # Para linha atual (0), é melhor vir da outra linha (1),
            # ou seja, passei pela linha 1 na estação est_at anterior
            caminho[0][est_at-1] = 1
            return vim_outra_linha
    else:
        # Recorro ao anterior da MESMA linha (linha=0, est_at=est_at-1)
        vim_msm_linha = caminho_mais_rapido(
            estacoes, trocas, entradas, 1, est_at-1, caminho)
        vim_msm_linha += estacoes[1][est_at]

        # Recorro ao anterior da OUTRA linha (linha=1, est_at=est_at-1)
        # aqui tem que considerar o custo de transferir de linha
        vim_outra_linha = caminho_mais_rapido(
            estacoes, trocas, entradas, 0, est_at-1, caminho)
        vim_outra_linha += estacoes[1][est_at] + trocas[0][est_at-1]
        # Pergunto, vim da msm linha é melhor? (melhor=menor custo)
        if vim_msm_linha <= vim_outra_linha:
            # Para linha atual (1), é melhor permanecer (1),
            # ou seja, passei pela linha 1 na estação est_at anterior
            caminho[1][est_at-1] = 1
            return vim_msm_linha
        else:
            # Para linha atual (0), é melhor vir da outra linha (1),
            # ou seja, passei pela linha 0 na estação est_at anterior
            caminho[1][est_at-1] = 0
            return vim_outra_linha


def resolver(estacoes, trocas, entradas, saidas, e):
    caminho = [
        [0 for i in range(e)],
        [0 for i in range(e)]
    ]

    # Calcula, o melhor caminho para quando se termina na linha 0
    melhor_lin0 = caminho_mais_rapido(
        estacoes, trocas, entradas, 0, e-1, caminho)
    # Calcula, o melhor caminho para quando se termina na linha 1
    melhor_lin1 = caminho_mais_rapido(
        estacoes, trocas, entradas, 1, e-1, caminho)

    custo_final_l0 = melhor_lin0 + saidas[0]
    custo_final_l1 = melhor_lin1 + saidas[1]

    # Pergunto, linha0 é a melhor?
    if custo_final_l0 <= custo_final_l1:
        caminho[0][e-1] = 0
        return custo_final_l0, caminho[0]
    else:
        caminho[1][e-1] = 1
        return custo_final_l1, caminho[1]
