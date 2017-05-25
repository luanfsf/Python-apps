
import os
import ansi_easy as AE

midhead  = "┌┴──────┬─────────────────────────────────────────────────────────────┴┐"
middle   = "├───────┼──────────────────────────────────────────────────────────────┤"
midend   = "└┬──────┴─────────────────────────────────────────────────────────────┬┘"

taskhead = "┌┴────────────────────────────────────────────────────────────────────┴┐"
taskend  = "└┬────────────────────────────────────────────────────────────────────┬┘"

prpthead = "┌┴───────────┬─────────────┬───────────────┬──────────────┬───────────┴┐"
prptend  = "└┬───────────┴─────────────┴───────────────┴──────────────┴───────────┬┘"

start    = "┌──────────────────────────────────────────────────────────────────────┐"
end      = "└──────────────────────────────────────────────────────────────────────┘"

endind   = "└──────────────────────────────────────────────────────────┬───────────┘"

def header(ntasks):

    ''' Exibe o número de tarefas e barra de uso'''

    spaces = " "* int(ntasks/2)
    if(ntasks != 100):
        usage = spaces + "{} ".format(AE.RST()) * (50-len(spaces))
    else:
        usage = spaces + AE.RST()

    print(start)
    print("│ TODOs │ {}{:<50} │ {:^3}/100 │".format(AE.BCK("GREEN"), usage, ntasks ) )
    print(taskend)

    return

def showTasks(todos):

    ''' Loop para exibir as tarefas e prioridades '''

    cores = {"1":"GREEN", "2":"YELLOW", "3":"RED"}

    blank = AE.RST()

    if ( len(todos.lista) > 0 ):
        print(midhead)

    for i in range(len(todos.lista)):
        # todos.lista[i][1] deve ser utilizado para fomatar a cor do
        cor = AE.COL( cores[todos.lista[i][1]] )
        col = "{}{}".format(AE.BCK("DEFAULT"), AE.BLD())
        print("│  {:^3}  │ {}{}{:<60}{} │".format(i+1, col, cor, todos.lista[i][0], blank ) ) # Incluir formatacao e cor da prioridade

        if (i == len(todos.lista) -1 ):

            print(midend)
            return

        print(middle)

    return

def endPrompt(todos): # Chama as funcoes da classe lista, mas não faz parte da classe lista

    print(prpthead)
    # print("│  1 Nova tarefa  │  2 Editar tarefa │  3 Excluir tarefa  │   4 Sair   │")
    print("│   1 Nova   │   2 Editar  │   3 Excluir   │   4 Ordenar  │   5 Sair   │")
    print(prptend, end="")

    executor(todos, options() )

    return

def options():

    opcoes = range(1,6)

    opc = int(input(AE.INV()))
    print(AE.RST(),end="")

    if ( opc not in opcoes ):

        opc = options()

    return opc

def executor(todos, opc):

    if ( opc == 1 ):

        if (todos.checklen() == 1 ):

            addTaskDecorator()
            todos.addTask()

        else:

            fullTasks()
            return

    elif ( opc == 2 ):

        if (todos.checkempty() == 1):

            noTasks()
            return

        else:
            editTaskDecorator()
            indice = int(input(AE.INV()))
            print(AE.RST(),end="")
            #print message being edited
            addTaskDecorator()

            if (todos.checkindex(indice) != 0):

                todos.editTask(indice)

                todos.saveDB()
        return

    elif ( opc == 3 ):

        if (todos.checkempty() == 1):
            noTasks()
            return
        else:
            removeTaskDecorator()
            indice = int(input())

            if (todos.checkindex(indice) != 0):

                todos.removeTask(indice)
                todos.saveDB()
        return

    elif ( opc == 4 ):

        if (todos.checkempty() == 1):
            noTasks()
            return
        else:
            todos.lista = sort(todos)

        return

    else:
        endMessage()
        exit()

#-------------------------------- Apenas Exibem um cabeçalho para as funções

def addTaskDecorator():

    print(taskhead)
    print("│ Digite uma tarefa que não ultrapasse o marcador abaixo.              │")
    print("│ Em seguida digite a prioridade  {}  1 NORMAL  {}  2 MÉDIA   {}   3 ALTA   {} │".format(AE.BCK("GREEN"), AE.BCK("YELLOW"), AE.BCK("RED"), AE.RST() ))
    print(endind)

    return

def editTaskDecorator():

    print(taskhead)
    print("│ Digite o indice da tarefa que deseja editar                          │")
    print(taskend, end="")

    return

def removeTaskDecorator():

    print(taskhead)
    print("│ Digite o indice da tarefa que deseja remover                         │")
    print(end, end="")

    return

def noTasks():

    print(taskhead)
    print("│ Não há itens na lista, pressione qualquer tecla para continuar       │")
    input(end + AE.INV())
    print(AE.RST())
    return

def fullTasks():

    print(start)
    print("│ Não há espaço para novos itens, remova alguns itens                  │")
    print(end)

    return

def endMessage():

    print(taskhead)
    print("│ Até logo! E conclua suas tarefas!!!                                  │")
    print(end)

    return

# UNIX-dos  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
# DOS only  (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )

def sort(todos): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    if (todos.lista == sorted(todos.lista, key=lambda x:x[1], reverse=True) ):
        return sorted(todos.lista, key=lambda x:x[0])
    return sorted(todos.lista, key=lambda x:x[1], reverse=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
