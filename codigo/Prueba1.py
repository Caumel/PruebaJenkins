import pandas as pd
import numpy as np


# Crear una calculadora para ejemplos faciles

def suma(a1,a2):
    resultado = a1 + a2
    return resultado

def resta(a1,a2):
    resultado = a1 - a2
    return resultado

def multiplicacion(a1,a2):
    resultado = a1 * a2
    return resultado

def division(a1,a2):
    if a2 == 0:
        raise ZeroDivisionError("You can't divide by zero")
    resultado = a1 / a2
    return resultado

def modulo(a1,a2):
    resultado = a1 % a2
    return resultado

def switch(argument,a1,a2):
    switcher = {
        '+': suma(a1,a2),
        '-': resta(a1,a2),
        'x': multiplicacion(a1,a2),
        '/': division(a1,a2),
        '%': modulo(a1,a2)
    }
    return switcher.get(argument, "Invalid operation")

def readoperation():
    operacion = input()
    a1, operador, a2 = operacion.split(' ')
    return a1,operador,a2
