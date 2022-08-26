import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores
import numpy as np

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    assert soma(1.0, 2.0) == 3.0

@pytest.mark.op_simples
def test_soma_dois_valores_negativos():
    assert soma(-1.0, -2.0) == -3.0

@pytest.mark.op_simples
def test_soma_dois_valores_iguais():
    assert soma(1.0, 1.0) == 2.0

@pytest.mark.op_simples
def test_sub_dois_valores_positivos():
    assert sub(1.0, 2.0) == -1.0

@pytest.mark.op_simples
def test_sub_dois_valores_negativos():
    assert sub(-1.0, -2.0) == 1.0

@pytest.mark.op_simples
def test_sub_dois_valores_iguais():
    assert sub(1.0, 1.0) == 0.0

@pytest.mark.op_simples
def test_multiplicacao_dois_valores_positivos():
    assert multiplicacao(1.0, 2.0) == 2.0

@pytest.mark.op_simples
def test_multiplicacao_dois_valores_negativos():
    assert multiplicacao(-1.0, -2.0) == 2.0

@pytest.mark.op_simples
def test_multiplicacao_dois_valores_iguais():
    assert multiplicacao(1.0, 1.0) == 1.0

@pytest.mark.op_complexas
def test_divisao_dois_valores_positivos():
    assert divisao(1.0, 2.0) == 0.5

@pytest.mark.op_complexas
def test_divisao_dois_valores_negativos():
    assert divisao(-1.0, -2.0) == 0.5

@pytest.mark.op_complexas
def test_divisao_dois_valores_iguais():
    assert divisao(1.0, 1.0) == 1.0

@pytest.mark.exercicio_1
def test_divisao_dois_valores_zero():
    assert np.inf == divisao(1.0, 0.0)

@pytest.mark.op_complexas
def test_media_lista_valores_positivos():
    assert media_lista_valores([1.0, 2.0, 3.0]) == 2.0

@pytest.mark.op_complexas
def test_media_lista_valores_negativos():
    assert media_lista_valores([-1.0, -2.0, -3.0]) == -2.0

@pytest.mark.op_complexas
def test_media_lista_valores_iguais():
    assert media_lista_valores([1.0, 1.0, 1.0]) == 1.0

@pytest.mark.op_complexas
def test_media_lista_valores_com_um_valor():
    assert media_lista_valores([1.0]) == 1.0

@pytest.mark.exercicio_1
def test_media_lista_valores_vazia():
    assert 0 == media_lista_valores([])

@pytest.mark.exercicio_1
def test_media_lista_valores_com_string():
    assert media_lista_valores([1.0, 2.0, 3.0, 'a', 5.0]) == 2.75