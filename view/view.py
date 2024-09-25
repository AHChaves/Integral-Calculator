import customtkinter as ctk
import entries as etr
import results as rst

def main():
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("425x525")
    root.title("Integral Calculator")
    root.resizable(False, False)
    root.minsize(425,525)

    Frame = ctk.CTkFrame(master=root)
    Frame.pack(fill="both", expand=True)
    Title = ctk.CTkLabel(master=Frame, text="Integral Calculator", font=("Roboto", 18))
    Title.pack(pady=12, padx=10, fill="x")
    
    Insert_frame = ctk.CTkFrame(Frame)
    Insert_frame.pack(fill="both", expand=True)
    
    Result_frame = ctk.CTkFrame(Frame)
    Result_frame.pack(fill="both", expand=True)
    
    etr.Insert_pane(Insert_frame, Result_frame)

    # rst.Results(Result_frame)
    
    root.mainloop()
