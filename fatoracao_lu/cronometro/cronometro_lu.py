import numpy as np

def tempo_lu(n, vetores, tempo_solucao, inicio_fatoracao, fim_fatoracao):
    # tempo para a solução, é executado múltiplas vezes por isso precisa somar
    tempo_total_fatoracao = fim_fatoracao - inicio_fatoracao
    tempo_total_solucao = np.sum(tempo_solucao)
    # tempo total é equivalente ao tempo de  uma fatoração mais a soma do tempo
    # de todas as soluções
    tempo_total = tempo_total_solucao + tempo_total_fatoracao

    tempo_medio = np.mean(tempo_solucao)
    tempo_min = np.min(tempo_solucao)
    tempo_max = np.max(tempo_solucao)

    print(f"Matriz {n}x{n} e {vetores} vetores de {n} índices:")
    print(f"\n  Tempo gasto no total:{tempo_total:.6f}s")
    print(f"  Tempo gasto na fatoração:{tempo_total_fatoracao:.6f}s")
    print(f"  Tempo gasto para {vetores} soluções:{tempo_total_solucao:.6f}s")
    print(f"  Tempo médio para solução: {tempo_medio * 1000:.6f}ms")
    print(f"  Melhor tempo para solução: {tempo_min * 1000:.6f}ms")
    print(f"  Pior tempo para solução: {tempo_max * 1000:.6f}ms")
    print(f"  Variação: {((tempo_max-tempo_min) * 1000):.6f}ms\n")

    return tempo_total, tempo_total_fatoracao, tempo_total_solucao
