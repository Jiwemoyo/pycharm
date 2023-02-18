# Widgets o componentes

# Frame:Sirve para posicionar y agrupar objetos como un div em html

import sys
import tkinter
from tkinter import ttk
import random

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

frame = ttk.Frame(window)

label = ttk.Label(frame, text='hola')
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

frame.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
sys.exit()  # terminal la ejection del gui no se ejecta lo que esta debajo en el gui
