import tkinter as tk

ventana=tk.Tk()
ventana.title("Codificacion")
ventana.geometry('380x300')
ventana.configure(background="dark turquoise")

e1=tk.Label(ventana, text="Numero 1:", bg="pink", fg="white")
e1.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X, padx=5, pady=4, ipadx=5, ipady=5)
ventana.mainloop()