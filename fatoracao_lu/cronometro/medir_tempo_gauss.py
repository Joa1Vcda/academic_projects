from ferramentas.gerar_matriz_valida import gerar_matriz_valida
from validações.validacao_gauss import eliminacao_gauss, substituicao
import numpy as np
import time
from . import cronometro_gauss as timer
import ferramentas.formatador as f

"""nesse arquivo não tem comprovações do resultado e nem precisa, todas as funções
chamadas aqui tem sua validação no próprio arquivo daonde vieram, ou seja:aqui é 
destinado somente para a medida de tempo sendo evitado poluir o terminal"""

"""todas as vezes que tiver um "gm." significa que estou usando uma função de 
"gerador_de_matrizes.py", caso precise de validação recomendo executa-lo
o mesmo ocorre com o "lu." que contém funções do arquivo lu.py"""

numero_de_vetores_por_tamanho = 1000

tamanho = [3, 10, 50, 100]
# print("Aquecendo o sistema pois a primeira execução tende a ser mais lenta:")
A = np.array([[2.0, 3.0, 1.0], [4.0, 7.0, 5.0], [6.0, 5.0, 2.0]])
b = np.array([3.0, 4.0, 5.0])
np.linalg.solve(A, b)


def multiplas_execucoes_gauss_com_tempo(tamanho, numero_de_vetores_por_tamanho):
    A = np.array([[2.0, 3.0, 1.0], [4.0, 7.0, 5.0], [6.0, 5.0, 2.0]])
    b = np.array([3.0, 4.0, 5.0])
    matriz_escalonada, vetor_modificado = eliminacao_gauss(A, b)
    substituicao(matriz_escalonada, vetor_modificado)
    tempo_total_gauss = []
    tempo_total_escalonamento = []
    tempo_total_solucao = []
    print("=== Teste usando eliminação de Gauss ===")
    for n in tamanho:
        tempo_solucao = []
        tempo_gauss = []
        vetor = 1
        matriz_aleatoria = gerar_matriz_valida(n)
        while vetor <= numero_de_vetores_por_tamanho:
            vetor_aleatorio = np.random.randint(0, 100, size=n).astype(float)
            inicio_gauss = time.perf_counter()  # inicia o contador de tempo
            matriz_escalonada, vetor_modificado = eliminacao_gauss(
                matriz_aleatoria, vetor_aleatorio
            )
            fim_gauss = time.perf_counter()  # termina o contador de tempo
            inicio_solucao = time.perf_counter()  # inicia o contador de tempo
            substituicao(matriz_escalonada, vetor_modificado)
            fim_solucao = time.perf_counter()  # termina o contador de tempo

            # soma o tempo de cada resolução de sistema
            tempo_solucao.append(fim_solucao - inicio_solucao)
            tempo_gauss.append(fim_gauss - inicio_gauss)
            vetor += 1

        tempo_total, tempo_total_eliminacao, tempo_total_substituicao = (
            timer.tempo_gauss(
                n, numero_de_vetores_por_tamanho, tempo_solucao, tempo_gauss
            )
        )
        tempo_total_gauss.append(tempo_total)
        tempo_total_escalonamento.append(tempo_total_eliminacao)
        tempo_total_solucao.append(tempo_total_substituicao)
    return tempo_total_gauss, tempo_total_escalonamento, tempo_total_solucao


if __name__ == "__main__":
    f.formatador()
    amarelo, verde, vermelho = multiplas_execucoes_gauss_com_tempo(
        tamanho, numero_de_vetores_por_tamanho
    )
