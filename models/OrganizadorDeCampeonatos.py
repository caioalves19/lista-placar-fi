class OrganizadorDeCampeonatos:
    ordem_categorias = ["Nacional", "Paulista", "Estadual", "Internacional", "Indefinido"]

    def __init__(self, lista_campeonatos):
        self.campeonatos = lista_campeonatos

    def exibir(self):
        string = ""
        for campeonato in self.campeonatos:
            string += f"{campeonato.nome}\n\n"

            for jogo in campeonato.jogos:
                if jogo.placar_penalti_mandante:
                    string += (f"{jogo.time_mandante} {jogo.placar_mandante} ({jogo.placar_penalti_mandante}) x ("
                              f"{jogo.placar_penalti_visitante}) {jogo.placar_visitante} {jogo.time_visitante}")

                elif jogo.placar_mandante:
                    string += (f"{jogo.time_mandante} {jogo.placar_mandante} x {jogo.placar_visitante} "
                              f"{jogo.time_visitante}")

                else:
                    string += f"{jogo.time_mandante} x {jogo.time_visitante}"

                if jogo.status_ao_vivo:
                    string += " (EM ANDAMENTO)"

                string += "\n"
            string += "\n"
        return string

    def ordenar_campeonatos(self):
        self.campeonatos.sort(
            key=lambda campeonato: (self.ordem_categorias.index(campeonato.categoria), campeonato.nome))
