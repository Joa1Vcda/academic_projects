import numpy as np
from ferramentas.gerar_matriz_valida import gerar_matriz_valida
from validacoes.validacao_lu import Solucionadorlu, fatoralu, verificacao_lu
import ferramentas.formatador as f

"""O que eu quero avaliar é comparar uma matriz com vários vetores diferentes que é exatamente aonde a fatoração LU ganha da eliminação de Gauss, para isso eu coloco a fatoração dentro de um loop for e a solução de sistemas dentro de um while que está dentro do for da fatoração, é um pouco complexo mas em resumo:uma matriz se relaciona com vários vetores, assim que a quantidade de vetores chegar ao valor desejado, o compilador volta para o loop for e muda o tamanho da matriz e dos vetores, então é se criado mais uma matriz só que com tamanho maior e logo depois é fatorada, depois disso mais vetores serão criados para se relacionar com essa matriz, isso vai ocorrer em todos os tamanhos desejados, caso queira ver a validação,execute em main.py"""


def multiplas_execucoes_lu(tamanhos, numero_de_vetores_por_tamanho):
    for n in tamanhos:
        vetor = 1
        A = gerar_matriz_valida(n)
        L, U = fatoralu(A)
        while vetor <= numero_de_vetores_por_tamanho:
            b = np.random.randint(1, 10, size=(n)).astype(float)
            solucao = Solucionadorlu(L, U, b)
            print(f"\n==={vetor}º Vetor para a matriz {n}x{n}===\n")
            verificacao_lu(A, b, L, U, solucao)
            vetor += 1
