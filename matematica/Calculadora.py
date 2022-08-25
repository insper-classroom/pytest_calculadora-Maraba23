import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    '''
    return va / vb if vb != 0 else np.inf

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores
    '''
    if len(v) == 0:
        return 0
    else:
        v = [x for x in v if not isinstance(x, str)]
        return np.mean(v)
