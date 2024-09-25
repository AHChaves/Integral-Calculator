import customtkinter as ctk

Frame = ctk.CTkFrame
soma_riemann = ctk.CTkLabel

# def Get_Frame(Frame):
#     global frame
#     frame = Frame


# def Results(frame):
#     global soma_riemann, Frame
    
#     Frame = frame
    
#     fontepadrao = ctk.CTkFont(family="Roboto", size=16)

#     soma_riemann = ctk.CTkLabel(master=frame, text="O resultado da soma de riemann é", font=fontepadrao)
#     soma_riemann.pack(padx=10, pady=5, anchor='w')
    
def Set_Results(Soma_Riemann, frame):
    
    global soma_riemann
    # global frame
    print(Soma_Riemann)
    # soma_riemann.configure(text=Soma_Riemann)
    soma_riemann = ctk.CTkLabel(master=frame, text=Soma_Riemann, font=("Roboto",16))
    soma_riemann.pack(padx=10, pady=5, anchor='w')