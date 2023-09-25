import pytest

from exercicio2 import menu




def test_valor_soma_cachorroQuente_e_cachorrQuenteDuplo():
    assert menu([100, 1, 101, 2]) == 20

def test_valor_cachorro_quente():
    assert menu([100, 2]) == 9   

def test_valor_cachorro_quente_duplo():
    assert menu([101, 2]) == 11      
   
def test_valor_x_egg():
    assert menu([102, 2]) == 12     
    
def test_valor_x_salada():
    assert menu([103, 2]) == 12   

def test_valor_x_bacon():
    assert menu([104, 2]) == 14

def test_valor_x_tudo():
    assert menu([105, 2]) == 17

def test_valor_refrigerante_lata():
    assert menu([200, 2]) == 5

def test_valor_cha_gelado():
    assert menu([201, 2]) == 4

def test_passando_por_um_valor_invalido():
    assert menu([500, 201, 2]) == 4