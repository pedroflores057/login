
from tkinter import *
ventana=Tk()
ventana.config(bg="#3CB371")
miFrame=Frame (ventana, width=200, height=200)
miFrame.pack()
la1=Label(miFrame, text="usuario:")
la1.grid(row=0, column=0, pady=10, padx=10)

la2=Label(miFrame, text="password::")
la2.grid(row=1, column=0, pady=10, padx=10)
txt1=Entry(miFrame, justify="center")
txt1.grid(row=0, column=1, pady=10, padx=10)
txt2=Entry(miFrame, show="*")
txt2.grid(row=1, column=2, pady=10, padx=10)

ba=Button(miFrame, text="login")
ba.grid(row=2, column=1, pady=10, padx=10)
ba.config(width=10)
ventana.mainloop()
