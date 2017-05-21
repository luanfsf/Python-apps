
import os
import ansi_easy as AE

midhead  = "┌┴──────┬─────────────────────────────────────────────────────────────┴┐"
middle   = "├───────┼──────────────────────────────────────────────────────────────┤"
midend   = "└┬──────┴─────────────────────────────────────────────────────────────┬┘"

taskhead = "┌┴────────────────────────────────────────────────────────────────────┴┐"
taskend  = "└┬────────────────────────────────────────────────────────────────────┬┘"

prpthead = "┌┴────────────────┬──────────────────┬────────────────────┬───────────┴┐"
prptend  = "└┬────────────────┴──────────────────┴────────────────────┴───────────┬┘"

start    = "┌──────────────────────────────────────────────────────────────────────┐"
end      = "└──────────────────────────────────────────────────────────────────────┘"

def header(ntasks):

    ''' Exibe o número de tarefas e barra de uso'''

    # print(AE.BLD(),end="")
    # print(AE.BCK("BLUE"),end="")
    # print(AE.COL("GREEN"),end="")

    print(start)
    print("│ TODOs │                                                    │ {:^3}/100 │".format( ntasks ) )
    print(taskend)

    return

def showTasks(todos):

    ''' Loop para exibir as tarefas e prioridades '''

    if ( len(todos.lista) > 0 ):
        print(midhead)

    for i in range(len(todos.lista)):
        # todos.lista[i][1] deve ser utilizado para fomatar a cor do
        print("│  {:^3}  │ {:^60} │".format( i+1, todos.lista[i][0]) ) # Incluir formatacao e cor da prioridade

        if (i == len(todos.lista) -1 ):

            print(midend)
            return

        print(middle)

    return

def endPrompt(todos): # Chama as funcoes da classe lista, mas não faz parte da classe lista

    print(prpthead)
    print("│  1 Nova tarefa  │  2 Editar tarefa │  3 Excluir tarefa  │   4 Sair   │")
    print(prptend, end="")

    executor(todos, options() )

    return

def options():

    opcoes = range(1,5)

    opc = int(input())

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

        editTaskDecorator()
        indice = int(input())

        if (todos.checkindex(indice) != 0):

            todos.editTask(indice)

            todos.saveDB()

    elif ( opc == 3 ):

        if (todos.checkempty() == 1):
            noTasks()
            return

        removeTaskDecorator()
        indice = int(input())

        if (todos.checkindex(indice) != 0):

            todos.removeTask(indice)
            todos.saveDB()

    else:
        exit()

#-------------------------------- Apenas Exibem um cabeçalho para as funções

def addTaskDecorator():

    print(taskhead)
    print("│ Digite uma tarefa de no máximo 60 characteres                        │")
    print("│ Em seguida digite a prioridade da tarefa 1, 2, 3                     │")
    # print("|**********************************************************|           |") # 60 CHARACTERES
    print(end)

    return

def editTaskDecorator():

    print(taskhead)
    print("│ Digite o indice da tarefa que deseja editar                          │")
    print(end, end="")

    return

def removeTaskDecorator():

    print(taskhead)
    print("│ Digite o indice da tarefa que deseja remover                         │")
    print(end, end="")

    return

def noTasks():

    print(start)
    print("│ Não há itens na lista                                                │")
    print(end)

    return

def fullTasks():

    print(start)
    print("│ Não há espaço para novos itens, remova alguns itens                  │")
    print(end)

    return

# UNIX-dos  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
# DOS only  (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )

def sort(): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
