import re

# Inicializa as listas para armazenar os monômios, coeficientes, expoentes e derivadas
monomios = []

def separar_monomios(string_do_usuario):
    monomios.clear()

    if string_do_usuario[0] not in '+-':
        string_do_usuario = '+' + string_do_usuario

    mon = re.findall(r'[+-]?\d*x\^\d+|[+-]?\d*x|[+-]?\d+', string_do_usuario)

    for x in mon:
        monomios.append(x)

    return mon

def calcularFuncao(array, numero):
    somaFuncao = 0
    first_term = True
    for x in array:
        if array[0] == x and first_term == True and x[0] == '+':
            x = x.replace("+", "")
        if first_term == True and x[0] == '-' and x[1] == 'x':
           x = x.replace('x', f'({numero})')
           x = x.replace('^', '**')
           somaFuncao += eval(x)
        elif x[0] == '+' and x[1] == 'x':
            x = x.replace('x', f'({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        elif x[0] == '-' and x[1] == 'x':
            x = x.replace('x', f'({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        elif x[0] == 'x':
            x = x.replace('x', f'({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        else:
            x = x.replace('x', f'*({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        first_term = False
    return somaFuncao

def Somatorio(a, init, end, delta_X):
    soma = 0
    for i in range(init, end):
        ponto = a + i*delta_X
        funcao_no_ponto = calcularFuncao(monomios, ponto)
        soma += funcao_no_ponto * delta_X
        
    return soma, ponto

def Calcula_Integral(funcao, a, b, n, loc):
    delta_X = (b-a)/n
    
    separar_monomios(funcao)
    if loc == "esquerda":
        soma, ponto = Somatorio(a, 0, n-1, delta_X)
    else:
        soma, ponto = Somatorio(a, 1, n, delta_X)

    return "O resultado da soma de riemann é " + '{0:.5g}'.format(soma), "O valor de delta x é " + format(delta_X), "O valor do ponto x(i) é: " + format(ponto)
                                                                                                                                                                   
if __name__ == '__main__':
    Calcula_Integral()