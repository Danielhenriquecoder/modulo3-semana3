import pytest
from exercicio3 import calcular_multiplicador_peso, ler_dimensoes_objeto, calcular_preco_volume, validar_medida, ler_rota, calcular_multiplicador_rota, calcular_frete, ler_peso_objeto

#testando função ler_dimensoes_objeto
def test_ler_dimensoes_objeto():
    assert ler_dimensoes_objeto([10, 10, 10]) == 20

#testando função calcular_preco_volume
def test_calcular_preco_volume_menor_que_1000_no_limite_menor():
    assert calcular_preco_volume (1) == 10

def test_calcular_preco_volume_menor_que_1000_no_limite_maior():
    assert calcular_preco_volume (999) == 10

def test_calcular_preco_volume_1000_menor_que_10000_no_limite_menor():
    assert calcular_preco_volume (1000) == 20

def test_calcular_preco_volume_1000_menor_que_10000_no_limite_maior():
    assert calcular_preco_volume (9999) == 20

def test_calcular_preco_volume_10000_menor_que_30000_no_limite_menor():
    assert calcular_preco_volume (10000) == 30

def test_calcular_preco_volume_10000_menor_que_30000_no_limite_maior():
    assert calcular_preco_volume (29999) == 30

def test_calcular_preco_volume_30000_menor_que_100000_no_limite_menor():
    assert calcular_preco_volume (30000) == 20

def test_calcular_preco_volume_30000_menor_que_100000_no_limite_maior():
    assert calcular_preco_volume (99999) == 20

# testando função validar_medida
def test_validar_medida():
    assert validar_medida (10) == 10

def test_validar_medida_entrando_com_objeto_nao_numerico():
    assert validar_medida ('error') == -1

#testando ler_peso_objeto
def test_ler_peso_objeto():
    assert ler_peso_objeto(40) ==  1

#testando função multiplicador_de_peso
def test_calcular_multiplicador_de_peso_menor_que_0_ponto_1():
    assert calcular_multiplicador_peso(0.0) == 1

def test_calcular_multiplicador_de_peso_0_ponto_1_menor_que_1_no_limite_menor():
    assert calcular_multiplicador_peso(0.1) == 1.5

def test_calcular_multiplicador_de_peso_0_ponto_1_menor_que_1_no_limite_maior():
    assert calcular_multiplicador_peso(0.9) == 1.5

def test_calcular_multiplicador_de_peso_1_menor_que_10_no_limite_menor():
    assert calcular_multiplicador_peso(1) == 2

def test_calcular_multiplicador_de_peso_1_menor_que_10_no_limite_maior():
    assert calcular_multiplicador_peso(9) == 2

def test_calcular_multiplicador_de_peso_10_menor_que_30_no_limite_menor():
    assert calcular_multiplicador_peso(10) == 3

def test_calcular_multiplicador_de_peso_10_menor_que_30_no_limite_maior():
    assert calcular_multiplicador_peso(30) == 3

#testando ler_rota 
def test_ler_rota_BR ():
    assert ler_rota("BR") == 1.5

def test_ler_rota_RB ():
    assert ler_rota("RB") == 1.5

def test_ler_rota_SB ():
    assert ler_rota("SB") == 1.2

def test_ler_rota_BS ():
    assert ler_rota("BS") == 1.2

def test_ler_rota_SR ():
    assert ler_rota("SR") == 1

def test_ler_rota_RS ():
    assert ler_rota("RS") == 1


#testando função calcular_multiplicador_de_rota
def test_calcular_multiplicador_rota_rs():
    assert calcular_multiplicador_rota('rs') == 1

def test_calcular_multiplicador_rota_sr():
    assert calcular_multiplicador_rota('sr') == 1

def test_calcular_multiplicador_rota_bs():
    assert calcular_multiplicador_rota('bs') == 1.2

def test_calcular_multiplicador_rota_SB():
    assert calcular_multiplicador_rota('sb') == 1.2

def test_calcular_multiplicador_rota_br():
    assert calcular_multiplicador_rota('br') == 1.5

def test_calcular_multiplicador_rota_rb():
    assert calcular_multiplicador_rota('rb') == 1.5

#testando função calcular_frete

def test_calcular_frete():
    assert calcular_frete(10,1,1.5) == 15
