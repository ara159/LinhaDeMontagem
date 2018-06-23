from sys import argv
from random import randint
from . import linha_dinamico, linha_recursivo


def imprimir_estacoes(f, l):
    print("Estaçoes:", len(l))
    print("Custo total (menor caminho):", f)
    print("Caminho:", l)


def resultados(custo_final, caminho, t):
    if not "--sem-result" in argv:
        imprimir_estacoes(custo_final, caminho)

    if "--custo" in argv:
        if "a" in t:
            print("Custo 'Divisão e conquista':", linha_recursivo.contador)
        if "b" in t:
            print("Custo 'Programação dinâmica':", linha_dinamico.contador)

    print()


def chamador():
    if "--aleatorio" in argv:
        n = int(argv[argv.index("--aleatorio")+1])
        estacoes = [[randint(5, 20) for i in range(n)],
                    [randint(5, 20) for i in range(n)]]
        trocas = [[randint(5, 20) for i in range(n-1)],
                  [randint(5, 20) for i in range(n-1)]]
        entradas = [randint(1, 10) for i in range(2)]
        saidas = [randint(1, 10) for i in range(2)]
    else:
        estacoes = [[7, 9, 3, 4, 8, 4],
                    [8, 5, 6, 4, 5, 7]]
        trocas = [[2, 3, 1, 3, 4],
                  [2, 1, 2, 2, 1]]
        entradas = [2, 4]
        saidas = [3, 2]
        n = 6

    if "--debug" in argv:
        print("Debug:")
        print("  Estações:", estacoes, "\n  Trocas:", trocas,
              "\n  Entradas:", entradas, "\n  Saidas:", saidas, "\n")

    todos = True
    if "--div-conq" in argv or "--dinamico" in argv:
        todos = False

    if todos or "--div-conq" in argv:
        if "--debug" in argv:
            print("### Divisão e conquista ###")
        custo_final, caminho = linha_recursivo.resolver(
            estacoes, trocas, entradas, saidas, n)
        resultados(custo_final, caminho, "a")
    if todos or "--dinamico" in argv:
        if "--debug" in argv:
            print("### Programação dinâmica ###")
        custo_final, caminho = linha_dinamico.caminho_mais_rapido(
            estacoes, trocas, entradas, saidas, n)
        resultados(custo_final, caminho, "b")
