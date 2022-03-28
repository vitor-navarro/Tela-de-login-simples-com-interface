from tkinter import Tk, Label, Button, Entry
from tkinter.ttk import Separator
from functools import partial
from core import logar

def tela_login():

    janela = Tk()
    janela.title("Tela de Login")

    separador = Separator(janela, orient='horizontal')
    separador.pack(fill='x')


    titulo_banco = Label(separador, text="Titulo", font=("Roboto", 25))
    titulo_banco.grid(column = 0, row=0, padx= 20, pady = 20)


    label_login = Label(separador, text="Login", font=("Roboto", 15), justify="left")
    label_login.grid(column = 0, row=1, sticky="w", padx=10)
    entry_login = Entry(separador, font=("Roboto", 15), justify="left")
    entry_login.grid(column = 0, row=2, padx = 10, pady=3)

    label_senha = Label(separador, text="Senha", font=("Roboto", 15), justify="left")
    label_senha.grid(column = 0, row=3, sticky="w", padx=10)
    entry_senha = Entry(separador, font=("Roboto", 15), justify="left")
    entry_senha.grid(column = 0, row=4, padx = 10, pady=3)

    login_args = partial(logar,entry_login.get, entry_senha.get) #para poder passar argumentos antes de chamar a função
    button_logar = Button(separador, text="Logar", command= login_args, font=("Roboto", 15), justify="center")
    button_logar.grid(column = 0, row = 5, padx = 5,pady = 10)

    janela.mainloop()

if __name__ == '__main__':
    tela_login()