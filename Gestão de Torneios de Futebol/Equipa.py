from Jogador import Jogador


class Equipa:
    def __init__(self, nome: str, treinador: str, jogadores: list):
        self.nome = nome
        self.treinador = treinador
        self.jogadores = jogadores


    def adicionarJogador(self, jogador: Jogador):
        self.jogadores.append(jogador)
