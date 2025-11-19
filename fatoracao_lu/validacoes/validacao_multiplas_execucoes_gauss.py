import numpy as np
from validacoes.validacao_gauss import eliminacao_gauss, substituicao, verificacao_gauss
from ferramentas.gerar_matriz_valida import gerar_matriz_valida
import ferramentas.formatador as f

"""O que eu quero avaliar é comparar uma matriz com vários vetores diferentes que é exatamente aonde a fatoração LU ganha da eliminação de Gauss, a eliminação de Gauss eu tenho que colocar dentro do loop while pois a cada vetor gerado é necessário uma nova eliminação de Gauss a solução de sistemas deve estar dentro do mesmo while que está dentro do for cuja função é apenas gerar uma matriz para cada tamanho, é um pouco complexo mas em resumo:uma matriz se relaciona com vários vetores, assim que a quantidade de vetores chegar ao valor desejado, o compilador volta para o loop for e muda o tamanho da matriz e dos vetores, então é se criado mais uma matriz só que com tamanho maior, depois disso mais vetores serão criados para se relacionar com essa matriz, isso vai ocorrer em todos os tamanhos desejados, caso queira ver a validação,execute em main.py"""

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

