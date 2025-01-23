class Campeonato:
    estaduais = ["amazonense", "acreano", "alagoano", "amapaense", "baiano", "brasiliense", "capixaba", "carioca",
                 "catarinense", "cearense", "gaúcho", "goiano", "maranhense", "mato-grossense", "sul-mato-grossense",
                 "mineiro", "paraense", "paraibano", "paranaense", "pernambucano", "piauiense", "potiguar",
                 "rondoniense", "roraimense", "sergipano", "tocantinense"]

    internacionais = ["alemão", "espanhol", "francês", "inglês", "italiano", "português", "saudita",
                      "liga dos campeões", "liga europa", "liga das nações", "copas internacionais"]

    nacionais = ["brasileirão", "copa do nordeste", "copa do brasil", "copa verde", "supercopa do rei"]

    paulistas = ["paulistão", "paulista", "são paulo"]

    filtros_categorias = [("Paulista", paulistas), ("Nacional", nacionais), ("Internacional", internacionais),
                          ("Estadual", estaduais)]

    def __init__(self, nome):
        self.nome = nome
        self.jogos = []
        self.categoria = self.definir_categoria()

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def definir_categoria(self):
        # Verificar as categorias específicas primeiro
        for categoria, filtros in self.filtros_categorias:
            if any(filtro in self.nome.lower() for filtro in filtros):
                return categoria

        # Caso nenhuma categoria seja encontrada
        return "Indefinido"
