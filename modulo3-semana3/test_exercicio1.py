import pytest

from exercicio1 import desconto 

def test_desconto_5_no_limite():
    assert desconto(100, 10) == (950.0, 1000)
def test_desconto_5_no_meio():    
    assert desconto(150, 20) == (2850.0, 3000)
def test_desconto_5_no_limite_com_valor_maior():
    assert desconto(1000, 10) == (9500.0, 10000)

def test_desconto_10_no_limite():
    assert desconto(100, 100) == (9000, 10000)
def test_desconto_10_no_meio():
    assert desconto(100,200 ) == (18000, 20000)

def test_desconto_15_no_limite():
    assert desconto(100,  1000) == (85000, 100000)   
def test_desconto_15_no_meio():
    assert desconto(100,2000 ) == (170000, 200000)   
    
def test_sem_desconto():
    assert desconto(100,5 ) == (500 ,500)