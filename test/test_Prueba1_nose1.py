
# # https://docs.python.org/3/library/unittest.html

# import unittest
# from codigo.Prueba1 import *
# from nose2.tools import params

# # Los archivos de test deben empezar por la palabra test

# # Se ejecuta nose2 y busca test

# class TestStrings(unittest.TestCase):

#     def test_suma(self):
#         self.assertEqual(suma(1,1), 2)

#     def test_resta(self):
#         self.assertEqual(resta(1,1), 0)

#     def test_multiplicacion(self):
#         self.assertEqual(multiplicacion(2,3), 6)

#     def test_division(self):
#         self.assertEqual(division(10,2), 5)

#     def test_modulo(self):
#         self.assertEqual(modulo(10,2), 0)


# @params("Sir Bedevere", "Miss Islington", "Duck")
# def test_is_knight(value):
#     assert value.startswith('Sir')

# assertEqual(a, b)   a == b
# assertNotEqual(a, b)  a != b

# assertTrue(x)   bool(x) is True
# assertFalse(x)  bool(x) is False

# assertIs(a, b)  a is b
# assertIsNot(a, b)    a is not b
# assertIsNone(x)   x is None
# assertIsNotNone(x)    x is not None
# assertIn(a, b)   a in b
# assertNotIn(a, b)   a not in b
# assertIsInstance(a, b)    isinstance(a, b)
# assertNotIsInstance(a, b)   not isinstance(a, b)