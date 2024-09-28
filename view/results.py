import customtkinter as ctk

def Set_Results(Soma_Riemann, frame, delta_x, val_ponto):
    
    delta_x = ctk.CTkLabel(master=frame, text=delta_x, font=("Roboto",16))
    delta_x.pack(padx=10, pady=5, anchor='w')
    
    ponto =  ctk.CTkLabel(master=frame, text=val_ponto, font=("Roboto",16))
    ponto.pack(padx=10, pady=5, anchor='w')
    
    soma_riemann = ctk.CTkLabel(master=frame, text=Soma_Riemann, font=("Roboto",16))
    soma_riemann.pack(padx=10, pady=5, anchor='w')