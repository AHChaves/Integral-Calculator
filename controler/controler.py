#import results as rst
from model import calc as clc
from view import results as rst

def Frame_Cleaner(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

def Calcula_Integral(funcao, inicio, fim, divisoes, loc_ponto, frame):
    if funcao != "":
        init = int(inicio)
        end = int(fim)
        n = int(divisoes)
        
        resultado = clc.Calcula_Integral(funcao, init, end, n, loc_ponto)
        
        Frame_Cleaner(frame)
        
        rst.Set_Results(resultado, frame)