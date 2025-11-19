import numpy as np

def tempo_gauss(n, vetores, tempo_solucao, tempo_gauss):
    # nesse caso é necessário fazer a soma das soluções e da eliminação, diferentemente
    # do código de fatoração LU no qual a fatoração só ocorre uma vez
    tempo_total_solucao = np.sum(tempo_solucao)
    tempo_total_escalonamento = np.sum(tempo_gauss)

    tempo_total = tempo_total_solucao + tempo_total_escalonamento

    tempo_medio = np.mean(tempo_solucao)
    tempo_min = np.min(tempo_solucao)
    tempo_max = np.max(tempo_solucao)

    print(f"Matriz {n}x{n} e {vetores} vetores de {n} índices:")
    print(f"\n  Tempo gasto no total:{tempo_total:.6f}s")
    print(f"  Tempo gasto na eliminação de Gauss:{tempo_total_escalonamento:.6f}s")
    print(f"  Tempo gasto para {vetores} soluções:{tempo_total_solucao:.6f}s")
    print(f"  Tempo médio para solução: {tempo_medio * 1000:.6f}ms")
    print(f"  Melhor tempo para solução: {tempo_min * 1000:.6f}ms")
    print(f"  Pior tempo para solução: {tempo_max * 1000:.6f}ms")
    print(f"  Variação: {((tempo_max-tempo_min) * 1000):.6f}ms\n")

    return tempo_total,tempo_total_escalonamento,tempo_total_solucao
