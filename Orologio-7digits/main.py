"""
Orologio-7digits
https://github.com/GHOSTRIDER5155/Progettini.git
"""
from datetime import datetime
import time
import tkinter as tk

root = tk.Tk()
root.title("Orologio")
root.geometry("400x200")

ora_label = tk.Label(root, font=("Arial", 24), fg= "green", bg= "black")
ora_label.pack()

def aggiorna_ora():
    ora = datetime.now().strftime("%H:%M:%S")
    ora_label.config(text=ora)
    root.after(1000, aggiorna_ora)

aggiorna_ora()
