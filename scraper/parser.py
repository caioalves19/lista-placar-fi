from models.Campeonato import Campeonato
from models.Jogo import Jogo


def parser_itens_placar(itens_placar):
    def montar_jogo():
        jogo = Jogo(jogo_atual["mandante"], jogo_atual["visitante"], jogo_atual["status_ao_vivo"])

        if "placar_mandante" in jogo_atual:
            jogo.placar_mandante = jogo_atual["placar_mandante"]
            jogo.placar_visitante = jogo_atual["placar_visitante"]

        if "placar_penalti_mandante" in jogo_atual:
            jogo.placar_penalti_mandante = jogo_atual["placar_penalti_mandante"]
            jogo.placar_penalti_visitante = jogo_atual["placar_penalti_visitante"]

        campeonato_atual.adicionar_jogo(jogo)

    # Criar lista para armazenar os campeonatos
    campeonatos = []
    campeonato_atual = None
    jogo_atual = {}

    for item in itens_placar:

        item_class = item.get_attribute("class")

        if item_class == "scoreboard__tag":
            if item.text.lower() == "ao vivo":
                jogo_atual["status_ao_vivo"] = True
            else:
                jogo_atual["status_ao_vivo"] = False

        elif item_class == "subheader__title":
            campeonato_atual = Campeonato(item.text)
            campeonatos.append(campeonato_atual)

        elif item_class == "scoreboard__result penalti":
            if not "placar_penalti_mandante" in jogo_atual:
                jogo_atual["placar_penalti_mandante"] = item.text
            else:
                jogo_atual["placar_penalti_visitante"] = item.text

        elif "scoreboard__team-name" in item_class:
            if not "mandante" in jogo_atual:
                jogo_atual["mandante"] = item.text  # Iniciar jogo com o time mandante
            else:
                jogo_atual["visitante"] = item.text  # Completar jogo com o time visitante
                montar_jogo()
                jogo_atual = {}

        elif "score-away" in item_class:
            if "placar_mandante" not in jogo_atual:
                jogo_atual["placar_mandante"] = item.text  # Placar do mandante
            elif "placar_visitante" not in jogo_atual:
                jogo_atual["placar_visitante"] = item.text  # Placar do visitante

    return campeonatos
