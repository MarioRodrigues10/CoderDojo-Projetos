from tkinter import *

def click(event):
    global valorEcra
    texto = event.widget.cget("text")
    if texto == "=":
        if valorEcra.get().isdigit():
            valor = int(valorEcra.get())
        else:
            valor = eval(screen.get())

        valorEcra.set(valor)
        screen.update()
    elif texto == "C":
         valorEcra.set("")
         screen.update()
    else:
        valorEcra.set(valorEcra.get() + texto)
        screen.update()

ecra = Tk()
ecra.geometry("600x650")
ecra.minsize(600, 650)
ecra.maxsize(600, 650)
ecra.config(bg="gray")
ecra.title("Calculadora")


valorEcra = StringVar()
valorEcra.set("")
f = Frame(ecra, padx=20,pady=20)
screen = Entry(f, textvar= valorEcra, font="lucida 50 bold", bg="light blue")
screen.pack(fill=X,padx=20,pady=15)
f.pack()

#Linhas
opcoes1 = ["7","8","9","+"]
opcoes2 = ["4","5","6","-"]
opcoes3 = ["1","2","3","*"]
opcoes4 = ["0","C","=","/"]

f = Frame(ecra, bg="gray",padx=30,pady=10)
for i in opcoes1:
     b = Button(f, text=i, padx=10,pady=10,font="lucida 25 bold")
     b.pack(side=LEFT,padx=10, pady=10)
     b.bind("<Button-1>",click)
f.pack()

f = Frame(ecra, bg="gray",padx=30,pady=10)
for i in opcoes2:
     b = Button(f, text=i, padx=10,pady=10,font="lucida 25 bold")
     b.pack(side=LEFT,padx=10, pady=10)
     b.bind("<Button-1>",click)
f.pack()

f = Frame(ecra, bg="gray",padx=30,pady=10)
for i in opcoes3:
     b = Button(f, text=i, padx=10,pady=10,font="lucida 25 bold")
     b.pack(side=LEFT,padx=10, pady=10)
     b.bind("<Button-1>",click)
f.pack()

f = Frame(ecra, bg="gray",padx=30,pady=10)
for i in opcoes4:
     b = Button(f, text=i, padx=10,pady=10,font="lucida 25 bold")
     b.pack(side=LEFT,padx=10, pady=10)
     b.bind("<Button-1>",click)
f.pack()


ecra.mainloop()

