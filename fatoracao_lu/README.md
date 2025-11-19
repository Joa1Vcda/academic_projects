# fatoracao_lu

Olá, meu nome é João Vitor Cirqueira de Araújo e sou um estudante do Instituto Federal do Maranhão-IFMA campus Imperatriz, esse código foi feito para a apresentação de um palestra cujo titúlo é: FATORAÇÃO LU: UMA ANÁLISE COMPARATIVA COM A ELIMINAÇÃO DE GAUSS o evento no qual vai ser apresentado é o IV SEPEF 01/12/2025, fui responsável pela apresentação,alguns afazeres na montagem do artigo e pela implementação do código,o código tem como principal objetivo resolver um sistema com matrizes aleatórias a cada tamanho N e M vetores diferentes para cada tamanho, por exemplo: comparar uma matriz 3x3 com 1000 vetores aleatórios de índice 3, e se eu aumentar o tamanho para 10x10 vai ser criada mais uma matriz 10x10 e compara-lá com 1000 vetores diferentes de indíce 10, e após isso construir um gráfico comparativo do tempo gasto para resolução de um sistema entre a fatoração L.U. e Eliminação de Gauss

Infelizmente eu sou muito indisciplinado com meu Git-Hub e acabei não separando em commits os processos que eu realizei mas vou deixar um resuminho em ordem cronológica de como foi feito, mas se for o caso de apenas executar, basta ler o tópico 1.

1. arquivo main.py

Arquivo onde é importado todos módulos, lá você define o tamanho no qual você deseja definir para as matrizes e consequente para os vetores no "tamanhos_N", e define quantos vetores diferentes você deseja no "numero_de_vetores_por_tamanho", no terminal sendo printado os tempos para cada marcaçao de tamanho, e então depois de executar ele mostra os gráficos, no total vão ser três gráficos, um de tempo total, um de tempo gasto só na preparação e um de tempo gasto só na solução, recomendo matrizes de até 200x200 para ter a percebção da diferença, mas bom... eu executei para matrizes 1000x1000 e demorou um pouco mais de 35 minutos somente na eliminação de Gauss, então é bom tomar cuidado na hora de selecionar os tamanhos, o tempo de execução pode variar de hardware para hardware e para situações de modo desempenho/múltiplos processos e etc

2. Pasta validacoes

2.1 Primeiramente eu fui atrás de fontes que poderiam me ajudar, após uma procura necessária eu cheguei no "Cálculo Numérico: um livro colaborativo (Versão Python)", lá eu copiei a função de fatoração L.U no qual o arquivo exato é o fatora_lu além disso: tive que ir atrás de como fazer a eliminação de Gauss, tive como base a função encontrada no livro "Laboratório Numérico(em python)", tive que fazer modificações para que ela tivesse o mesmo comportamento da fatora_lu, e para isso tiver que separa em duas partes, uma só de eliminação e outra só para substituição inversa, e então isso me deu a ideia: "e se eu comparar o tempo de cada etapa e não somente o tempo total?" complicou um pouco mais mas cheguei no resultado que gostaria, mas voltando apenas na implementação da fatoração L.U e de Gauss meu primeiro trabalho foi validar se a funções que havia criado/modificado/aproveitado e para isso eu fiz uma função cujo objetivo era printar os resultados para facilitar a comparação com a matriz original e o vetor original.

2.2. Após eu ter validado a eficiência de apenas uma execução eu precisei seguir adiante e fazer a validação para múltiplos vetores diferentes, nesse etapa eu notei um problema, as funções tinham uma limitação, elas não previam pivotamento parcial, fazendo com que algumas matrizes não tivessem resolução e então eu tive que construir uma função geradora de matrizes(que se encontra na pasta de ferramentas), ela funciona da seguinte forma: cria uma matriz aleatória e tenta fatorar sem pivotamento, se ela conseguir então retorna a matriz aleatória, se ela não conseguir então cria uma matriz nova e repete esse processo até um número máximo de vetores diferentes.

2.3. Agora com a função geradora de matrizes eu voltei para validação, segui um processo parecido da execução única, meu maior trabalho foi pensar no loop for, como queria apenas uma matriz e vários vetores diferentes por tamanho, eu optei por um loop while dentro de um loop for, a lógica é parecida tanto para Gauss quanto para fatoração L.U, a principal diferença é que na fatoração L.U era necessário apenas uma fatoração para cada matriz e consequentemente para cada tamanho, mas no caso de Gauss, é obrigatório fatorar a cada vetor diferente, isso ocorre porque na fatoração L.U o vetor não modifica a fatoração, mas o vetor afeta no processo de eliminação de Gauss, então no caso a função fatora_lu deve ficar no for(que modifica o tamanho), enquanto a eliminação de Gauss deve ficar dentro do while(que gera os vetores exigidos), essa lógica é o que faz a fatoração L.U ser a melhor escolha para casos de vários vetores

3. Pasta cronometro

É aqui onde é medido o tempo, foi utilizado a biblioteca time e a função time.perf_counter() para calcular, bom aqui a lógica não é muito diferente da lógica de múltiplas execuções, as principais diferenças é que eu não preciso conferir se está correto pois já fiz isso em outra pasta,e que o timer deve acompanhar o que ele quer calcular o tempo de execução, depois de somar o tempo de execução e o tempo de preparação eu somo esses dois para obter o tempo total,a geração de matrizes e de vetores não entram no contador, apenas o processo de solução do sistema 

4. Pasta graficos

Aqui é montado o gráfico, nada muito complicado, a biblioteca matploblita faz o trabalho sujo enquanto você oferece os valores a partir do retorno das funções da pasta cronometro, para cada gráfico é oferecido o retorno específico do que ele deve representar 

5. Pasta ferramentas

Bom, aqui tem apenas a função de gerar matriz aleatoria e o formatador de prints pra evitar notação ciéntifica e valores com muitas casa decimais 

6. Referências bibliográficas

MIRANDA, Pedro M. A. Laboratório Numérico (em python). Versão 2018/03/01. [S.l.: s.n.], 2018.

JUSTO, Dagoberto Adriano Rizzotto; SAUTER, Esequia; AZEVEDO, Fabio Souto de; GUIDI, Leonardo Fernandes; KONZEN, Pedro Henrique de Almeida. Cálculo Numérico: um livro colaborativo (Versão Python). Porto Alegre: UFRGS, 2020. Disponível em: https://www.ufrgs.br/reamat. Acesso em: 18 nov. 2025.






MIRANDA, Pedro M. A. Laboratório Numérico (em python). Versão 2018/03/01. [S.l.: s.n.], 2018.
