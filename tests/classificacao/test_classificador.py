from app.classificacao.classificador import classificar_nota, calcular_desconto

def test_nota_invalida_abaixo_de_zero():
    assert classificar_nota(-1) == "nota invalida"

def test_nota_invalida_acima_de_dez():
    assert classificar_nota(11) == "nota invalida"

def test_nota_aprovada():
    assert classificar_nota(8) == "aprovado"

def test_nota_em_recuperacao(): 
    assert classificar_nota(5.5) =="recuperacao"

def test_nota_reprovada():
    assert classificar_nota(3) == "reprovado"



def test_valor_invalido():
    assert calcular_desconto(-10, False) == -1


def test_cliente_vip():
    assert calcular_desconto(100, True) == 20


def test_cliente_normal_com_desconto():
    assert calcular_desconto(200, False) == 20


def test_cliente_sem_desconto():
    assert calcular_desconto(50, False) == 0

    