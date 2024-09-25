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

def Calcula_Integral(funcao, a, b, n):
    delta_X = (b-a)/n
    
    separar_monomios(funcao)
    soma = 0
    for i in range(1, n):
        ponto_dir= i/n
        funcao_no_ponto = calcularFuncao(monomios, ponto_dir)
        soma += funcao_no_ponto * delta_X

    return "O resultado da soma de riemann é " + '{0:.4g}'.format(soma)
    
if __name__ == '__main__':
    Calcula_Integral()