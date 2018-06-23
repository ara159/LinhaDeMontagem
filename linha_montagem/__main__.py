from sys import argv
from linha_montagem import chamador

if __name__ == "__main__":
    if "--ajuda" in argv:
        print(
            "== LINHA DE MONTAGEM == \
Uso: \
    python3 -m "+argv[0]+" [parâmetros]\n \
Parâmetros disponíveis \
--aleatorio n: Executa com valores aleatórios e com n estações \
--custo: Imprime o custo \
--sem-result: Executa, porém não imprime a saída \
--debug: Imprime todas as estruturas de dados de parametro \
--dinamico: Executa somente o algoritmo na forma dinâmica \
--div-conq: Executa somente o algoritmo na forma divisão e conquista")
        exit(2)
    chamador()
