from tkinter import *

janela = Tk()
janela.title('PyFoot')
janela['background']='green'
janela.geometry('500x500+100+100')

lb=Label(janela, text="Betania")
lb.place(x=100, y=100)

janela.mainloop()
