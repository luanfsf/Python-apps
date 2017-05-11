# UNIX-dos  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
# DOS only  (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )

import os
import ansi_easy as AE

def header(todos):
    ''' Exibe o número de tarefas e barra de uso'''
    print("┌───────┬────────────────────────────────────────────────────┬─────────┐")
    print("│ TODOs │                                                    │ {3}/100 │")
    print("└┬──────┴────────────────────────────────────────────────────┴────────┬┘")

midhead = "┌┴──────┬─────────────────────────────────────────────────────────────┴┐"
middle =  "├───────┼──────────────────────────────────────────────────────────────┤"
midend =  "└┬──────┴─────────────────────────────────────────────────────────────┬┘"


start  = "┌──────────────────────────────────────────────────────────────────────┐"
end    = "└──────────────────────────────────────────────────────────────────────┘"

def showTasks(todos):
    ''' Loop para exibir as tarefas e prioridades '''

    print(midhead)
    for i in range(len(todos.lista)):
        # todos.lista[i][1] deve ser utilizado para fomatar a cor do
        print("│  {:^3}  │ {:^60} │".format( i+1, todos.lista[i][0]) ) # Incluir formatacao e cor da prioridade
        if (i == len(todos.lista) -1 ):
            print(midend)
        else:
            print(middle)
    return

def endPrompt(todos): # Chama as funcoes da classe lista, mas não faz parte da classe lista
    print("┌┴────────────────┬──────────────────┬────────────────────┬───────────┴┐")
    print("│  1 Nova tarefa  │  2 Editar tarefa │  3 Excluir tarefa  │   4 Sair   │")
    print("└┬────────────────┴──────────────────┴────────────────────┴───────────┬┘")

    opcoes = [1,2,3,4]
    opc = 0

    while( opc not in opcoes ):
        opc = int(input())

    if ( opc == 1 ):

        if (todos.checklen() == 1 ):
            addTaskDecorator()
            todos.addTask()
        else:
            fullTasks()

        todos.saveDB()

    elif ( opc == 2 ):

        if (todos.checkempty() == 1):
            noTasks()

        if (todos.editTask.indice() != 0)
            todos.editTask()
            editTaskDecorator()

        todos.saveDB()

    elif ( opc == 3 ):

        if (todos.checkempty() == 1):

        removeTaskDecorator()
        todos.removeTask()
        todos.saveDB()

    else:
        todos.saveDB()
        exit()
#-------------------------------- Apenas Exibem um cabeçalho para a função
def addTaskDecorator():

    print(midhead)
    print("│ Adicionar tarefa de no máximo 60 characteres                         │")
    # print("|**********************************************************|           |") # 60 CHARACTERES
    print(midend)

    return

def editTaskDecorator():

    print(midhead)
    print("│ Digite o indice da tarefa que deseja editar                          │")
    print(midend)

    return

def removeTaskDecorator():

    print(start)
    print("│ Digite o indice da tarefa que deseja remover                         │")
    print(end)

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

#--------------------------------

def sort(): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
