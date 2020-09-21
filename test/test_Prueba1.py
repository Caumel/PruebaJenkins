# El nombre del archivo debe de ser test_


import pytest
from codigo.Prueba1 import *

def test_sum():   # Deben empezar por test_
    assert suma(1,1) == 2

def test_res():   # Deben empezar por test_
    assert resta(1,1) == 0

def test_mul():   # Deben empezar por test_
    assert multiplicacion(2,3) == 6

def test_div():   # Deben empezar por test_
    assert division(10,5) == 2

def test_mod():   # Deben empezar por test_
    assert modulo(10,4) == 2

def test_zero_division():  # Forma para hacer test con excepciones
    with pytest.raises(ZeroDivisionError): 
        division(1,0)



# #Pytest fixtures

# #Antes 

# # test_wallet.py

# import pytest
# from wallet import Wallet, InsufficientAmount


# def test_default_initial_amount():
#     wallet = Wallet()
#     assert wallet.balance == 0

# def test_setting_initial_amount():
#     wallet = Wallet(100)
#     assert wallet.balance == 100

# def test_wallet_add_cash():
#     wallet = Wallet(10)
#     wallet.add_cash(90)
#     assert wallet.balance == 100

# #Despues

# # test_wallet.py

# import pytest
# from wallet import Wallet, InsufficientAmount

# @pytest.fixture
# def empty_wallet():
#     '''Returns a Wallet instance with a zero balance'''
#     return Wallet()

# @pytest.fixture
# def wallet():
#     '''Returns a Wallet instance with a balance of 20'''
#     return Wallet(20)

# def test_default_initial_amount(empty_wallet):
#     assert empty_wallet.balance == 0

# def test_setting_initial_amount(wallet):
#     assert wallet.balance == 20

#pytest --fixtures # Nos da una descripcion de los fixures que hay si hemos puesto un comentario en el metodo


# Llamar a pytest desde python
pytest.main()

# @pytest.fixture
# def error_fixture():
#     assert 0


# def test_ok():
#     print("ok")


# def test_fail():
#     assert 0


# def test_error(error_fixture):
#     pass


# def test_skip():
#     pytest.skip("skipping this test")


# def test_xfail():
#     pytest.xfail("xfailing this test")


# @pytest.mark.xfail(reason="always xfail")
# def test_xpass():
#     pass