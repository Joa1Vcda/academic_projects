import numpy as np
from ferramentas.gerar_matriz_valida import gerar_matriz_valida
import ferramentas.formatador as f

matriz_a = gerar_matriz_valida(n=3)
vetor_b = np.array([1.0, 3.0, 4.0])


def eliminacao_gauss(matriz_a, vetor_b):
    n = matriz_a.shape[0]
    copia_a = np.copy(matriz_a)
    copia_b = np.copy(vetor_b)
    for k in range(n - 1):
        if matriz_a[k, k] == 0:
            return None, None
        for j in range(k + 1, n):
            e = copia_a[j, k] / copia_a[k, k]
            copia_a[j, k:] = copia_a[j, k:] - e * copia_a[k, k:]
            copia_b[j] = copia_b[j] - e * copia_b[k]
    return copia_a, copia_b

def substituicao(matriz_a, vetor_b):
    n = len(matriz_a)
    x = [0.0] * n  

    for k in range(n - 1, -1, -1):

        soma = 0.0
        for j in range(k + 1, n):
            soma += matriz_a[k][j] * x[j]

        x[k] = (vetor_b[k] - soma) / matriz_a[k][k]
    return x

def verificacao_gauss(
    matriz_original, vetor_original, matriz_escalonada, vetor_modificado, solucao
):
    print(f"\n1. Matriz Original A:\n", matriz_original)
    print(f"\n2. Vetor Original b:\n", vetor_original)
    print(f"\n3. Matriz Escalonada:\n", matriz_escalonada)
    print(f"\n4. Vetor Modificado:\n", vetor_modificado)
    print(f"\n5. Solução X:\n{solucao}")

    verificacao = np.dot(matriz_original, solucao)
    print(f"\n6. Verificação (A*x):\n {verificacao}")
    print(
        f"\n7. a Verificação acima deve ser igual ao vetor b original:\n {vetor_original}"
    )

if __name__ == "__main__":
    f.formatador()
    copia_a, copia_b = eliminacao_gauss(matriz_a, vetor_b)
    solucao = substituicao(copia_a, copia_b)
    solucao_np = np.array(solucao)
    verificacao_gauss(matriz_a, vetor_b, copia_a, copia_b, solucao_np)
