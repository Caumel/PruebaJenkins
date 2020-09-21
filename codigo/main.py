from codigo.Prueba1 import readoperation,switch

while True:
    print('''
############################
Que operacion desea realizar

    + : Suma
    - : Resta
    x : Multiplicación
    / : División
    % : Módulo

    Ejemplo: 5 x 7
    
    ''')

    a1, operador, a2 = readoperation()

    print()
    print('Resultado: ', switch(operador,int(a1),int(a2)))
    print()
    print('############################')