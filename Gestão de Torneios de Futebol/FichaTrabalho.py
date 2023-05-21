# Tema 1 – Gestão de Torneios de futebol

from Equipa import Equipa
from Jogador import Jogador
from Jogo import Jogo

NUMJOGADORES = 15
equipas = []

def inserirInfoEquipas():
    equipaNome = input("Indique o nome da equipa:\n")
    treinadorNome = input("Indique o nome do treinador:\n")
    equipa = Equipa(equipaNome, treinadorNome, [])
    for x in range(NUMJOGADORES):
        jogadorNome = input("Indique o nome do jogador:\n")
        jogadorIdade = int(input("Indique a idade do jogador:\n"))
        jogadorNumero = int(input("Indique o número do jogador:\n"))
        jogador = Jogador(jogadorNome, jogadorIdade, jogadorNumero)
        equipa.adicionarJogador(jogador)
    equipas.append(equipa.nome)

def alterarInfoEquipas():




def eliminarInfoEquipas():



while True:
    menu_escolhas_x, menu_escolhas_y = \
        (input("Inserir (A), alterar(B) ou eliminar(C)"
              " informação? Das equipas(X) "
              "ou dos jogos(Y)? Fechar(Z).\n").lower()).split(" ")
    match menu_escolhas_x:
        case "a":
            inserirInfoEquipas()
        case "b":
            alterarInfoEquipas()
        case "c":
            eliminarInfoEquipas()
        case "z":
            break