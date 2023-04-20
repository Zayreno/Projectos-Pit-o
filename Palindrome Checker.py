palavra = input("Por favor indique a sua palavra:\n")
palavraLen = len(palavra) - 1
posicao = 0
falhou = False

while posicao <= palavraLen // 2:
    print(F"{palavra[posicao]} - {palavra[palavraLen - posicao]}")
    if palavra[posicao] != palavra[palavraLen - posicao]:
        falhou = True
        break
    posicao += 1

if falhou == False:
    print("A sua palavra é um palíndromo!")
else:
    print("A sua palavra não é um palíndromo!")