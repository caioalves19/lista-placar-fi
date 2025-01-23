import tkinter
from tkinter import *
from tkinter import ttk

from models.OrganizadorDeCampeonatos import OrganizadorDeCampeonatos
from scraper.scraper import scrape_jogos


class ListaJogosApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Lista de Jogos - Futebol Interior")
        self.janela_largura = 600
        self.janela_altura = 500

        self.configurar_tela_principal()
        self.configurar_estilos()

        self.dia_placar_var = StringVar()
        self.criar_widgets()
        self.window.mainloop()

    def configurar_tela_principal(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        pos_x = (screen_width - self.janela_largura) // 2
        pos_y = (screen_height - self.janela_altura) // 2
        self.window.geometry(f"{self.janela_largura}x{self.janela_altura}+{pos_x}+{pos_y}")
        self.window.resizable(False, False)
        self.window.columnconfigure(0, weight=1, uniform="a")
        self.window.rowconfigure(0, weight=1, uniform="a")

    def criar_widgets(self):
        mainframe = ttk.Frame(self.window, padding="0", style="Custom.TFrame")
        mainframe.grid(column=0, row=0, sticky="news")
        mainframe.columnconfigure((0, 1), weight=1, uniform="a")
        mainframe.rowconfigure(0, weight=2, uniform="a")
        mainframe.rowconfigure(1, weight=1, uniform="a")
        mainframe.rowconfigure(2, weight=8, uniform="a")

        titulo_label = ttk.Label(mainframe, text="Lista de Jogos - Futebol Interior", anchor="center",
                                 style="Custom.TLabel")
        titulo_label.grid(column=0, row=0, columnspan=2, sticky="news")

        dia_placar = ttk.Combobox(mainframe, textvariable=self.dia_placar_var, state="readonly", font=("Tahoma", 16),
                                  justify="center")
        dia_placar['values'] = ('Hoje', 'Amanhã')
        dia_placar.set(dia_placar['values'][0])
        dia_placar.grid(column=0, row=1, sticky="ew", padx="25", pady=5)

        buscar_button = ttk.Button(mainframe, text="Buscar", style="Custom.TButton", command=self.buscar_jogos)
        buscar_button.grid(column=1, row=1, sticky="ew", padx="25", pady=5)

        self.lista_texto = tkinter.Text(mainframe)
        self.lista_texto.grid(column=0, row=2, columnspan=2, sticky="news", padx="25", pady=10)
        self.lista_texto.config(state="disabled", font=("Consolas", 10))

    def buscar_jogos(self):
        dia_selecionado = self.dia_placar_var.get().lower()
        if dia_selecionado == "amanhã":
            dia_selecionado = "amanha"
        link = f"https://www.futebolinterior.com.br/placar-ao-vivo/?{dia_selecionado}"
        campeonatos = scrape_jogos(link)
        org = OrganizadorDeCampeonatos(campeonatos)
        org.ordenar_campeonatos()
        lista = org.exibir()

        self.lista_texto.config(state="normal")
        self.lista_texto.delete("1.0", "end")
        self.lista_texto.insert("1.0", lista)
        self.lista_texto.config(state="disabled")

    @staticmethod
    def configurar_estilos():
        style = ttk.Style()
        style.configure("Custom.TFrame", background="sea green")
        style.configure("Custom.TLabel", background="sea green", font=("Helvetica", 20), foreground="white")
        style.configure("Custom.TButton", font=("Tahoma", 15))
