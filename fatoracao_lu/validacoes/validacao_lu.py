import numpy as np
import ferramentas.formatador as f

"""este arquvio realiza passo a passo e apresenta verificação do resultado,como
vou fazer muitos testes onde o ideal é que eu saiba apenas o tempo,então vou importar
esse arquivo para servir como base, em outros arquivos usarei as funções que foram 
validadas por aqui só que sem a necessidade de retorna o resultado no terminal,
assim eu vou ter certeza que meu resultado está correto sem poluir o terminal"""


"""classe para facilitar a solução do sistema matriz_lower,matriz_upper com o vetor vetor_b"""

class Solucionadorlu:
    def __init__(self, matriz_lower, matriz_upper, vetor_b):
        self.matriz_lower = matriz_lower
        self.matriz_upper = matriz_upper
        self.vetor_b = vetor_b
        self.y = None
        self.x = None
        self.resolver()

    def resolver(self):
        n = len(self.matriz_lower)
        self.y = [0.0] * n

        for i in range(n):
            soma_l = 0.0
            for j in range(i):
                soma_l += self.matriz_lower[i][j] * self.y[j]
            self.y[i] = self.vetor_b[i] - soma_l

        self.x = [0.0] * n

        for i in range(n - 1, -1, -1):
            soma_u = 0.0
            for j in range(i + 1, n):
                soma_u += self.matriz_upper[i][j] * self.x[j]

            self.x[i] = (self.y[i] - soma_u) / self.matriz_upper[i][i]


matriz_A = np.array([[2.0, 3.0, 1.0], [4.0, 7.0, 5.0], [6.0, 5.0, 2.0]])  # matriz fixa
vetor_b = np.random.randint(0, 10, size=3).astype(
    float
)  # gerador de vetores aleatórios

"""Função "fatoralu" obtida do livro (Cálculo Numérico, 2020)"""
def fatoralu(matriz_A):
    matriz_upper = np.copy(matriz_A)
    n = np.shape(matriz_upper)[0]
    matriz_lower = np.eye(n)
    for j in np.arange(n - 1):
        for i in np.arange(j + 1, n):
            matriz_lower[i, j] = matriz_upper[i, j] / matriz_upper[j, j]
            for k in np.arange(j + 1, n):
                matriz_upper[i, k] = (
                    matriz_upper[i, k] - matriz_lower[i, j] * matriz_upper[j, k]
                )
            matriz_upper[i, j] = 0
    return matriz_lower, matriz_upper


def verificacao_lu(matriz_A, vetor_b, matriz_lower, matriz_upper, solucao):
    print("1. Definir a Matriz A:\n", matriz_A)

    print("\n2. Definir o Vetor b:\n ", vetor_b)

    print(f"\n3. RESOlUÇÃO DO SISTEMA Ax = b:")
    print(f"\nvalores de x:\n {np.round(solucao.x,2)}")
    print(f"\nvalores de y:\n {np.round(solucao.y,2)}")

    print("\n4. Verificação para conferir o valor da matriz lower e upper")
    print(
        "\nVerificação matriz lower * matriz upper :"
        f"\n{np.dot(matriz_lower, matriz_upper)}"
    )
    print(
        "\nA verificação acima deve resultar "
        f"a seguinte matriz aleatória:\n {matriz_A}"
    )

    print("\n5. Verificação para os valores de x e y:")
    verificacao_x = np.dot(matriz_A, solucao.x)
    print(f"\nVerificação: A * x = \n{verificacao_x}")

    verificacao_y = np.dot(matriz_lower, solucao.y)
    print(f"\nVerificação: matriz_lower * y = \n{verificacao_y}")

    print(
        "\nAs duas verificações acima devem resultar"
        f" no seguinte vetor b aleatório:\n{vetor_b}\n"
    )


def lu():
    f.formatador()
    matriz_lower, matriz_upper = fatoralu(matriz_A)
    solucao = Solucionadorlu(matriz_lower, matriz_upper, vetor_b)
    verificacao_lu(matriz_A, vetor_b, matriz_lower, matriz_upper, solucao)


if __name__ == "__main__":
    lu()
