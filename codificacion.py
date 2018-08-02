import tkinter as tk
import numpy
#Cofigurando ventana del programa
ventana=tk.Tk()
ventana.title("Cifrado de PlayFair")
ventana.geometry('680x400')
ventana.configure(background="dim gray")

#Funcion para cifrar
def cifrando():

    avanz=0
    #Tomar datos del Input1
    formato=str(entrada1.get())
    #Pasar todo a minusculas
    foma2=formato.lower()
    # Convertir a una lista temporal el texto
    cadenatxt=list(foma2)
    #Pasarlo a una lista ya declarada
    txtintro=[]
    for c in cadenatxt:
         txtintro.append(c)
    print(txtintro)
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
              "w", "x", "y", "z"]
    #Uniendo las dos listas
    txtintro.extend(letras)

    #Quitar los repetidos en orden
    lst2 = []
    [lst2.append(key) for key in txtintro if key not in lst2]
    #Insertando los datos de la palabra clave
    insertar_datos(lst2)
    #Organizando la frase para aplicar luego las reglas
    oracion=manejoMensaje()
    #Aplicando las reglas
    codifiya=reglas(oracion,lst2)
    #Retornando los valores de las variables
    return var.set(cadenatxt), var2.set(codifiya)
def manejoMensaje():
    # Tomar datos del Input2
    frase = str(entrada2.get())
    frasel = frase.lower()
    oralist = list(frasel)
    conta=0
    #Quitando Espacios en blanco
    for quie in oralist:
        if(quie==" "):
            oralist.remove(quie)
    #Quitar repetidos
    maxi=len(oralist)
    for nume in range(0,maxi):
        if(nume>0):
            if(oralist[nume-1]==oralist[nume]):
                oralist.pop(nume)
                oralist.insert(nume , "x")
    if(maxi%2==0):
        pass
    else:
        oralist.append("x")
    return oralist
#Reglas de oracion
def reglas(oraciont, listadatos):

    codificada=oraciont
    letras=listadatos
    if len(codificada)%2>0:
        codificada.append("x")
    lista1=listadatos[0:5]
    lista2=listadatos[5:10]
    lista3=listadatos[10:15]
    lista4=listadatos[15:20]
    lista5=listadatos[20:25]
    print(lista5)
    print(lista4)
    print(lista3)
    print(lista2)
    print(lista1)

    return codificada

def insertar_datos(txtlist):

    cell0.delete(0, tk.END)
    cell1.delete(0, tk.END)
    cell2.delete(0, tk.END)
    cell3.delete(0, tk.END)
    cell4.delete(0, tk.END)
    cell5.delete(0, tk.END)
    cell6.delete(0, tk.END)
    cell7.delete(0, tk.END)
    cell8.delete(0, tk.END)
    cell9.delete(0, tk.END)
    cell10.delete(0, tk.END)
    cell11.delete(0, tk.END)
    cell12.delete(0, tk.END)
    cell13.delete(0, tk.END)
    cell14.delete(0, tk.END)
    cell15.delete(0, tk.END)
    cell16.delete(0, tk.END)
    cell17.delete(0, tk.END)
    cell18.delete(0, tk.END)
    cell19.delete(0, tk.END)
    cell20.delete(0, tk.END)
    cell21.delete(0, tk.END)
    cell22.delete(0, tk.END)
    cell23.delete(0, tk.END)
    cell24.delete(0, tk.END)


    cell0.insert(0 ,txtlist[0])
    cell1.insert(0, txtlist[5])
    cell2.insert(0, txtlist[10])
    cell3.insert(0, txtlist[15])
    cell4.insert(0, txtlist[20])

    cell5.insert(0, txtlist[1])
    cell6.insert(0, txtlist[6])
    cell7.insert(0, txtlist[11])
    cell8.insert(0, txtlist[16])
    cell9.insert(0, txtlist[21])

    cell10.insert(0, txtlist[2])
    cell11.insert(0, txtlist[7])
    cell12.insert(0, txtlist[12])
    cell13.insert(0, txtlist[17])
    cell14.insert(0, txtlist[22])

    cell15.insert(0, txtlist[3])
    cell16.insert(0, txtlist[8])
    cell17.insert(0, txtlist[13])
    cell18.insert(0, txtlist[18])
    cell19.insert(0, txtlist[23])

    cell20.insert(0, txtlist[4])
    cell21.insert(0, txtlist[9])
    cell22.insert(0, txtlist[14])
    cell23.insert(0, txtlist[19])
    cell24.insert(0, txtlist[24])







def dibujando(dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12,dato13,dato14,dato15,
              dato16,dato17,dato18,dato19,dato20,dato21,dato22,dato23,dato24,dato25):
    # Mostrar resultado en labels 0

    cell0.grid(padx=20, pady=1, row=12, column=0)
    cell0.insert(0, dato1)
    cell1.grid(padx=20, pady=1, row=13, column=0)
    cell1.insert(0, dato2)
    cell2.grid(padx=20, pady=1, row=14, column=0)
    cell2.insert(0, dato3)
    cell3.grid(padx=20, pady=1, row=15, column=0)
    cell3.insert(0, dato4)
    cell4.grid(padx=20, pady=1, row=16, column=0)
    cell4.insert(0, dato5)

    # Mostrar resultado en labels  1

    cell5.grid(padx=20, pady=1, row=12, column=1)
    cell5.insert(0, dato6)
    cell6.grid(padx=20, pady=1, row=13, column=1)
    cell6.insert(0, dato7)
    cell7.grid(padx=20, pady=1, row=14, column=1)
    cell7.insert(0, dato8)
    cell8.grid(padx=20, pady=1, row=15, column=1)
    cell8.insert(0, dato9)
    cell9.grid(padx=20, pady=1, row=16, column=1)
    cell9.insert(0, dato10)

    # Mostrar resultado en labels  2

    cell10.grid(padx=20, pady=1, row=12, column=2)
    cell10.insert(0, dato11)
    cell11.grid(padx=20, pady=1, row=13, column=2)
    cell11.insert(0, dato12)
    cell12.grid(padx=20, pady=1, row=14, column=2)
    cell12.insert(0, dato13)
    cell13.grid(padx=20, pady=1, row=15, column=2)
    cell13.insert(0, dato14)
    cell14.grid(padx=20, pady=1, row=16, column=2)
    cell14.insert(0, dato15)

    # Mostrar resultado en labels  3

    cell15.grid(padx=20, pady=1, row=12, column=3)
    cell15.insert(0, dato16)
    cell16.grid(padx=20, pady=1, row=13, column=3)
    cell16.insert(0, dato17)
    cell17.grid(padx=20, pady=1, row=14, column=3)
    cell17.insert(0, dato18)
    cell18.grid(padx=20, pady=1, row=15, column=3)
    cell18.insert(0, dato19)
    cell19.grid(padx=20, pady=1, row=16, column=3)
    cell19.insert(0, dato20)

    # Mostrar resultado en labels  4

    cell20.grid(padx=20, pady=1, row=12, column=4)
    cell20.insert(0, dato21)
    cell21.grid(padx=20, pady=1, row=13, column=4)
    cell21.insert(0, dato22)
    cell22.grid(padx=20, pady=1, row=14, column=4)
    cell22.insert(0, dato23)
    cell23.grid(padx=20, pady=1, row=15, column=4)
    cell23.insert(0, dato24)
    cell24.grid(padx=20, pady=1, row=16, column=4)
    cell24.insert(0, dato25)


#------------------------------------------------Programa principal-------------------------------------
#Variable que retorna la cadena cifrada
var=tk.StringVar()
var2=tk.StringVar()
#Etiqueta 1
e1=tk.Label(ventana, text="Ingrese una palabra clave:(Sin Espacios)", bg="navy", fg="white")
e1.grid(row=1, column=0,pady=5,padx=5,columnspan=2)
#Etiqueta 2
e12=tk.Label(ventana, text="Mensaje a Cifrar ", bg="navy", fg="white")
e12.grid(row=1, column=1,pady=5,padx=5,columnspan=3)
#Input para ingreso de clave
entrada1=tk.Entry(ventana)
entrada1.grid(row=2, column=0,pady=20,padx=10,columnspan=2)
#Input para ingreso de Mensaje
entrada2=tk.Entry(ventana)
entrada2.grid(row=2, column=1,pady=20,padx=10,columnspan=3)
#Boton para ingresar datos
botonap=tk.Button(ventana,text="Ingresar Datos",fg="blue",command=cifrando,width=20)
botonap.grid(row=2, column=3,pady=5,columnspan=2)


#Label para mostrar el resultado cifrado
res=tk.Label(ventana, bg="sea green",textvariable=var, padx=5, pady=5, width="50")
res.grid(row=10, column=0,pady=10,columnspan=5)
#Label para mostrar el resultado cifrado
oracionr=tk.Label(ventana, bg="SpringGreen2",textvariable=var2, padx=5, pady=5, width="50")
oracionr.grid(row=18, column=0,pady=10,columnspan=5)

#Inicializar Arrays de Entry
cell0 = tk.Entry(ventana, width=10)
cell1 = tk.Entry(ventana, width=10)
cell2 = tk.Entry(ventana, width=10)
cell3 = tk.Entry(ventana, width=10)
cell4 = tk.Entry(ventana, width=10)
cell5 = tk.Entry(ventana, width=10)
cell6 = tk.Entry(ventana, width=10)
cell7 = tk.Entry(ventana, width=10)
cell8 = tk.Entry(ventana, width=10)
cell9 = tk.Entry(ventana, width=10)
cell10 = tk.Entry(ventana, width=10)
cell11 = tk.Entry(ventana, width=10)
cell12 = tk.Entry(ventana, width=10)
cell13 = tk.Entry(ventana, width=10)
cell14 = tk.Entry(ventana, width=10)
cell15 = tk.Entry(ventana, width=10)
cell16 = tk.Entry(ventana, width=10)
cell17 = tk.Entry(ventana, width=10)
cell18 = tk.Entry(ventana, width=10)
cell19 = tk.Entry(ventana, width=10)


cell20 = tk.Entry(ventana, width=10)
cell21 = tk.Entry(ventana, width=10)
cell22 = tk.Entry(ventana, width=10)
cell23 = tk.Entry(ventana, width=10)
cell24 = tk.Entry(ventana, width=10)
dato1=dato2=dato3=dato4=dato5=dato6=dato7=dato8=dato9=dato10=dato11=dato12=dato13=dato14=dato15=dato16=dato17=dato18=dato19=dato20=dato21=dato22=dato23=dato24=dato25=2
dibujando( dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8, dato9,dato10, dato11, dato12,
          dato13, dato14, dato15, dato16, dato17, dato18, dato19,dato20,dato21,dato22,dato23,dato24,dato25)

ventana.mainloop()

