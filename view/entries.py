import customtkinter as ctk
from controler import controler as ctr

class EntryWithLimitation(ctk.CTkEntry):
    def __init__(self, master, charlist, **kw):
        super().__init__(master, **kw)
        self.charlist = charlist

        text_checker = master.register(self.isValid)
        self.configure(validate="key", validatecommand=(text_checker, "%P"))

    def isValid(self, text):
        
        # Verifica se os caracteres estao na whitelist
        for char in text:
            if char not in self.charlist and not char.isdigit():
                return False
                
        # Verifica se há letras repetidas consecutivamente
        for i in range(len(text)-1):

            Sequntial =  text[i].lower().isalpha() and text[i].lower() == text[i + 1].lower()

            if Sequntial:
                return False
            
            numberAfterX = text[i].lower() == 'x' and (text[i+1].isnumeric() or text[i+1] not in self.charlist)

            if numberAfterX:
                return False
                
            if text[i].lower() != 'x' and text[i+1] == '^':
                return False

            if text[i] == '^' and text[i+1].lower() == 'x':
                return False

            if text[i] in '+-^' and text[i+1] in '+-^':
                return False

        return True


class EntryNumbers(ctk.CTkEntry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        text_checker = master.register(self.isValid)
        self.configure(validate="key", validatecommand=(text_checker, "%P"))

    def isValid(self, text):
        
        # Verifica se os caracteres estao na whitelist
        for char in text:
            if char == "-":
                return True
            if not char.isdigit():
                return False
                
        return True

def Insert_pane(frame, resultFrame):
    
    fontepadrao = ctk.CTkFont(family="Roboto", size=16)
    CharList = ["x", "X", "+", "-", "^"]

    frame.rowconfigure((0,1,2,3,4,5), weight=0)
    frame.columnconfigure((0,1), weight=0)
    
    inicio = ctk.CTkLabel(frame, text="inicio do intervalo:")
    inicio.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    inicio_etr = EntryNumbers(frame)
    inicio_etr.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    fim = ctk.CTkLabel(frame, text="fim do intervalo:")
    fim.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    fim_etr = EntryNumbers(frame)
    fim_etr.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    n_value = ctk.CTkLabel(frame, text="Escolha o numero de divisoes")
    n_value.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    
    n_value_opt = ctk.CTkOptionMenu(frame, 
                                values=["100", "300", "600", "1000", "1500", "2000"],)
    n_value_opt.grid(row=2, column=1, padx=10, pady=10)
    
    side = ctk.CTkLabel(frame, text="Escolha o lado do ponto")
    side.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    
    side_opt = ctk.CTkOptionMenu(frame, 
                                values=["esquerda", "direita"])
    side_opt.grid(row=3, column=1, padx=10, pady=10)
    
    funcao = ctk.CTkLabel(frame, text="informe a funcao a ser avaliada:",)
    funcao.grid(row=4,column=0, padx=10, sticky="e")
    
    funcao_etr = EntryWithLimitation(frame,CharList)
    funcao_etr.grid(row=5, column=0, sticky="we", padx=10)

    calculate_btn = ctk.CTkButton(frame, width=90, height=30, font=fontepadrao, text="Calculate", 
                                  command=lambda: ctr.Calcula_Integral(funcao_etr.get(), inicio_etr.get(), fim_etr.get(), n_value_opt.get(), resultFrame))
    calculate_btn.grid(row=5, column=1, sticky="e")