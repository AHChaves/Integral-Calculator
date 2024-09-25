#import results as rst
from model import calc as clc
from view import results as rst

def Calcula_Integral(funcao, inicio, fim, divisoes, frame):
    if funcao != "":
        init = int(inicio)
        end = int(fim)
        n= int(divisoes)
        
        resultado = clc.Calcula_Integral(funcao, init, end, n)
        
        rst.Set_Results(resultado, frame)