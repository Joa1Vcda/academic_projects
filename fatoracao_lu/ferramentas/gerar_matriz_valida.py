import numpy as np
import warnings
from validacoes.validacao_lu import fatoralu

"""O código de fatoração LU obtido em:(Cálculo Numérico, 2020) não faz uso de 
pivoteamento parcial,isso faz com que tenha casos onde a fatoração LU ou Gauss não 
sejam póssiveis de forma direta,e nesses casos é obtido um warning e consequentemente
se perde uma execução,então tive que criar uma função cujo principal objetivo é criar 
mais uma matriz ao indentificar um warning,e novamente tenta-se fatorar,esse processo 
pode ser repetido até obter uma matriz válida ou até chegar no max_tentativas, caso 
queira testes maiores que o padrão, recomendo aumentar o número max de tentativas, mas 
maioria das vezes vai ser desnecessário, além disso, ter um gerador sendo usado de 
paramêtro tanto para Gauss quanto para fatoração LU traz mais fidelidade a comparação"""

def gerar_matriz_valida(n, max_tentativas=100):
    for tentativa in range(max_tentativas):
        with warnings.catch_warnings():
            warnings.filterwarnings("error")
            try:
                A = np.random.randint(1, 100, size=(n, n)).astype(float)
                fatoralu(A)
                return A
            except:
                continue
    print("excedeu o número de tentativas, tente novamente")

