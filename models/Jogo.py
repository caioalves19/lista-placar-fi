class Jogo:
    def __init__(self, time_mandante, time_visitante, status_ao_vivo, placar_mandante=None, placar_visitante=None,
                 placar_penalti_mandante=None, placar_penalti_visitante=None):
        self.time_mandante = time_mandante
        self.time_visitante = time_visitante
        self.placar_mandante = placar_mandante
        self.placar_visitante = placar_visitante
        self.placar_penalti_mandante = placar_penalti_mandante
        self.placar_penalti_visitante = placar_penalti_visitante
        self.status_ao_vivo = status_ao_vivo
