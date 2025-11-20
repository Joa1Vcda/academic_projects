# fatoracao_lu
# Fatoração LU vs Eliminação de Gauss: Uma Análise Comparativa

Essa pasta do repositório contém o código fonte e os experimentos desenvolvidos para a apresentação no **IV SEPEF (01/12/2025)** do IFMA - Campus Imperatriz.

**Autor:** João Vitor Cirqueira de Araújo
**Instituição:** Instituto Federal do Maranhão (IFMA)

## 🎯 Objetivo
O projeto visa comparar o desempenho computacional (tempo de execução) entre dois métodos de resolução de sistemas lineares:
1.  **Fatoração LU**
2.  **Eliminação de Gauss**

A análise foca especificamente no cenário de **múltiplos vetores independentes** para uma mesma matriz de coeficientes, construindo gráficos comparativos de:
* Tempo total de execução.
* Tempo de preparação (fatoração/escalonamento).
* Tempo de solução (substituições).

## 🛠️ Estrutura do Projeto

O código foi organizado em módulos para facilitar a validação e a medição de tempo:

* **`main.py`**: Arquivo principal. Define os tamanhos das matrizes (`N`) e a quantidade de vetores, executa os testes e gera os gráficos.
* **`validacoes/`**: Aqui é onde é realizado a verificação de resultados Contém os algoritmos de Fatoração LU e Gauss sem o **pivotamento parcial** sendo exigido um gerador de matrizes solucionaveis encontrado na pasta ferramentas.
    * *Nota:* Para o método de Gauss, a implementação foi separada em eliminação e substituição para permitir a medição isolada dos tempos.
* **`cronometro/`**: Módulo responsável por medir o tempo de processamento utilizando `time.perf_counter()` para alta precisão.
* **`ferramentas/`**: Utilitários para gerar matrizes aleatórias (garantindo que sejam solucionáveis) e formatar a saída no terminal.
* **`graficos/`**: Gera as visualizações dos dados utilizando a biblioteca `matplotlib`.

## 🚀 Como Executar

### Pré-requisitos
Você precisará do Python instalado e das biblioteca `matplotlib` e da `numpy`, para facilitar tem o arquivo requirements.txt que possibilita a instalação de tudo de uma vez em um virtual environment.

```bash
pip install -r requirements.txt
```
## ‼️ Referências bibliográficas

MIRANDA, Pedro M. A. Laboratório Numérico (em python). Versão 2018/03/01. [S.l.: s.n.], 2018.

JUSTO, Dagoberto Adriano Rizzotto; SAUTER, Esequia; AZEVEDO, Fabio Souto de; GUIDI, Leonardo Fernandes; KONZEN, Pedro Henrique de Almeida. Cálculo Numérico: um livro colaborativo (Versão Python). Porto Alegre: UFRGS, 2020. Disponível em: https://www.ufrgs.br/reamat. Acesso em: 18 nov. 2025.






MIRANDA, Pedro M. A. Laboratório Numérico (em python). Versão 2018/03/01. [S.l.: s.n.], 2018.
