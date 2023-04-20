def darOpcoes():
    print("Quer criar(A), apagar(B) ou editar(C) a tarefa? Pode também fechar a aplicação(Sair). \n")

def escreverTopo():
    print("#####################\n###### TODO LIST ######")

def escreverTarefas(tarefas):
    for x in range(0, len(tarefas)):
        print(F"{x}. {tarefas[x]}")

def criarTarefa():
    cT = str(input("Descreva a tarefa:\n"))
    listaTarefas.append(cT)

def apagarTarefa():
    if len(listaTarefas) == 0:
        print("Não há tarefas disponíveis")
    else:
        aT = int(input("Escolha qual tarefa quer tirar:"))
        if aT > len(listaTarefas) - 1:
            print("Opção inválida")
        else :
            listaTarefas.pop(aT)

def editarTarefa():
    if len(listaTarefas) == 0:
        print("Não há tarefas disponíveis")
    else:
        eT = int(input("Escolha qual tarefa quer editar:"))
        if eT > len(listaTarefas) - 1:
            print("Opção inválida")
        else :
            eET = str(input("Descreva a nova tarefa:\n"))
            listaTarefas[eT] = eET

FILE_NAME = "test.csv"

def saveToFile(list):
    with open(FILE_NAME, 'w') as f:
        f.write('\n'.join(list))

def readFile():
    list = []
    try:
        with open(FILE_NAME, 'r') as f:
            for line in f:
                list.append(line.strip())
        return list
    except:
        return []

escolha = ("")
listaTarefas = readFile()

while escolha != "sair":
    escreverTopo()
    escreverTarefas(listaTarefas)
    darOpcoes()

    escolha = str(input(">> ")).lower()

    if escolha == "a":
        criarTarefa()
    elif escolha == "b":
        apagarTarefa()
    elif escolha == "c":
        editarTarefa()
    elif escolha == "sair":
        saveToFile(listaTarefas)
        print("Adios!")
    else:
        print("Escolha inválida")