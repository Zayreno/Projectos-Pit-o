import random

list = ["comer", "limpar", "viajar", "bombeiro", "guitarra", "praia", "camelo", "dromedario", "hipopotamo", "biblioteca"]
guess = []
randList = random.randint(0,len(list)-1)

randWord = list[randList]

randWordLen = len(randWord)

def letraEscolhidaNaTentativa():
    for letra in randWord:
        if letra in guess:
            print(letra, end="")
        else:
            print("_", end="")
    print("\n")

def seraQueJaSeEncontrouAPalavra():
    for letra in randWord:
        if letra not in guess:
            return False
    return True

while seraQueJaSeEncontrouAPalavra() == False:
    letraEscolhidaNaTentativa()
    guessChar = str(input("Guess a letter: \n"))
    guess.append(guessChar)

print(F"Congratulations, the word was \"{randWord}\"!")