import numpy as np

"""Função para formatar a saída de matrizes no terminal, definindo precisão e suprimindo notação científica."""


def formatador():
    np.set_printoptions(suppress=True, precision=2)
