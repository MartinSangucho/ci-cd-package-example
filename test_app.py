# test_app.py
import pytest
from app import sumar, multiplicar

def test_sumar_correcta():
    """Pruebo que la función sumar retorne el resultado correcto."""
    assert sumar(5, 3) == 8

def test_sumar_cero():
    """Pruebo la suma con cero."""
    assert sumar(10, 0) == 10

def test_sumar_negativos():
    """Pruebo la suma con números negativos."""
    assert sumar(-5, 2) == -3

def test_sumar_tipo_incorrecto():
    """Pruebo que sumar lance un TypeError si los tipos son incorrectos, como lo diseñé."""
    with pytest.raises(TypeError):
        sumar("a", 1)

def test_multiplicar_correcta():
    """Pruebo que la función multiplicar retorne el resultado correcto."""
    assert multiplicar(4, 2) == 8