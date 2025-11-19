import numpy as np
import time
from validacoes.validacao_lu import fatoralu, Solucionadorlu
from .cronometro_lu import tempo_lu as timer
from ferramentas.gerar_matriz_valida import gerar_matriz_valida
import ferramentas.formatador as f

numero_de_vetores_por_tamanho = 1000
tamanho = [3, 10, 50, 100]


def multiplas_execucoes_lu_com_tempo(tamanho, numero_de_vetores_por_tamanho):
    # Aquecendo o sistema pois a primeira execução tende a ser mais lenta
    A = np.array([[2.0, 3.0, 1.0], [4.0, 7.0, 5.0], [6.0, 5.0, 2.0]])
    matriz_lower, matriz_upper = fatoralu(A)
    tempo_total_lu = []
    tempo_total_fatoracao_lu = []
    tempo_total_solucao = []
    print("=== Teste usando Fatoração LU ===")
    for n in tamanho:
        tempo_solucao = []
        vetor = 1
        matriz_aleatoria = gerar_matriz_valida(n)

        inicio_fatoracao = time.perf_counter()  # inicia o contador de tempo
        matriz_lower, matriz_upper = fatoralu(matriz_aleatoria)
        fim_fatoracao = time.perf_counter()  # termina o contador de tempo
        while vetor <= numero_de_vetores_por_tamanho:
            vetor_b = np.random.randint(0, 100, size=n).astype(float)
            inicio_solucao = time.perf_counter()  # inicia o contador de tempo
            Solucionadorlu(matriz_lower, matriz_upper, vetor_b)
            fim_solucao = time.perf_counter()  # termina o contador de tempo

            # soma o tempo de cada resolução de sistema
            tempo_solucao.append(fim_solucao - inicio_solucao)
            vetor += 1
        # tempo para se realizar a fatoração (executa apenas uma vez por tamanho):

        tempo_total, tempo_total_fatoracao, tempo_total_substituicao = timer(
            n,
            numero_de_vetores_por_tamanho,
            tempo_solucao,
            inicio_fatoracao,
            fim_fatoracao,
        )
        tempo_total_lu.append(tempo_total)
        tempo_total_fatoracao_lu.append(tempo_total_fatoracao)
        tempo_total_solucao.append(tempo_total_substituicao)
    return tempo_total_lu, tempo_total_fatoracao_lu, tempo_total_solucao


if __name__ == "__main__":
    f.formatador()
    multiplas_execucoes_lu_com_tempo(tamanho, numero_de_vetores_por_tamanho)
