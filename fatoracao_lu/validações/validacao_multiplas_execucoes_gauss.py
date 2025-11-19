import numpy as np
from validações.validacao_gauss import eliminacao_gauss, substituicao, verificacao_gauss
from ferramentas.gerar_matriz_valida import gerar_matriz_valida
import ferramentas.formatador as f

tamanhos = [3, 10, 50, 100]
numero_de_vetores_por_tamanho = 5


def multiplas_execucoes_gauss(tamanhos, numero_de_vetores_por_tamanho):
    for n in tamanhos:
        vetor = 1
        matriz_aleatoria = gerar_matriz_valida(n)
        while vetor <= numero_de_vetores_por_tamanho:
            vetor_aleatorio = np.random.randint(0, 100, size=n).astype(float)
            matriz_escalonada, vetor_modificado = eliminacao_gauss(
                matriz_aleatoria, vetor_aleatorio
            )
            solucao = substituicao(matriz_escalonada, vetor_modificado)
            solucao_np = np.array(solucao)
            print(f"\n==={vetor}º Vetor para a matriz {n}x{n}===\n")
            verificacao_gauss(
                matriz_aleatoria,
                vetor_aleatorio,
                matriz_escalonada,
                vetor_modificado,
                solucao_np,
            )
            vetor += 1


if __name__ == "__main__":
    f.formatador()
    multiplas_execucoes_gauss(tamanhos, numero_de_vetores_por_tamanho)
