from cronometro.medir_tempo_gauss import (
    multiplas_execucoes_gauss_com_tempo as resolver_gauss,
)
from cronometro.medir_tempo_lu import multiplas_execucoes_lu_com_tempo as resolver_lu
from graficos.grafico_comparativo_fatoracao import montar_grafico_fatoracao
from graficos.grafico_comparativo_substituicao import montar_grafico_substituicao
from graficos.grafico_tempo_total import montar_grafico_tempo_total
from validacoes.validacao_multiplas_execucoes_gauss import multiplas_execucoes_gauss
from validacoes.validacao_multiplas_execucoes_lu import multiplas_execucoes_lu
from ferramentas.formatador import formatador

"""Função main para executar validações e medições de tempo comparativas entre Fatoração LU e Eliminação de Gauss.Para ver as validações, descomente as linhas correspondentes. Tenha responsabilidade ao executar múltiplas validações, pois elas podem gerar uma grande quantidade de saída no console."""

"""Além disso é possível ajustar os tamanhos das matrizes e o número de vetores por tamanho conforme necessário. Porém tome cuidado com valores muito altos, pois podem causar lentidão."""


def main():
    # Definir tamanhos e número de vetores por tamanho
    tamanhos_N = [3, 25, 50, 75, 100]
    numero_de_vetores_por_tamanho = 1000

    # Executar múltiplas validações
    print("Validação Múltipla - Fatoração LU")
    multiplas_execucoes_lu(tamanhos_N, numero_de_vetores_por_tamanho)
    print("\nValidação Múltipla - Eliminação de Gauss")
    multiplas_execucoes_gauss(tamanhos_N, numero_de_vetores_por_tamanho)

    # Medir tempos
    x, y, z = resolver_lu(tamanhos_N, numero_de_vetores_por_tamanho)
    tempo_total_lu = x
    tempo_fatoracao_lu = y
    tempo_substituicao_lu = z

    x, y, z = resolver_gauss(tamanhos_N, numero_de_vetores_por_tamanho)
    tempo_total_gauss = x
    tempo_eliminicao_gauss = y
    tempo_substituicao_gauss = z

    montar_grafico_substituicao(
        tempo_substituicao_lu, tempo_substituicao_gauss, tamanhos_N
    )

    montar_grafico_fatoracao(tempo_fatoracao_lu, tempo_eliminicao_gauss, tamanhos_N)

    montar_grafico_tempo_total(tempo_total_lu, tempo_total_gauss, tamanhos_N)


formatador()
main()
