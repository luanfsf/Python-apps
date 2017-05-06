# UNIX-dos  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
# DOS only  (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )

import os
import ansi_easy as AE

def header(todos):
    ''' Exibe o número de tarefas e barra de uso'''

    print("┌───────┬────────────────────────────────────────────────────┬─────────┐")
    print("│ TODOs │                                                    │ {3}/100 │")
    print("└┬──────┴────────────────────────────────────────────────────┴────────┬┘")

def showTasks(todos):
    ''' Loop para exibir as tarefas e prioridades '''

    print("┌┴──────┬─────────────────────────────────────────────────────────────┴┐")
    for i in range(len(todos.lista)):
        # todos.lista[i][1] deve ser utilizado para fomatar a cor do
        print("│  {:^3}  │ {:^60} │".format( i+1, todos.lista[i][0]) ) # Incluir formatacao e cor da prioridade
        if (i == len(todos.lista) -1 ):
            print("└┬──────┴─────────────────────────────────────────────────────────────┬┘")
        else:
            print("├───────┼──────────────────────────────────────────────────────────────┤")
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

        if (todos.addTask.check() == 1 ):
            addTaskDecorator()
            todos.addTask()
        else:
            addTaskDecorator("Full")

        todos.saveDB()

    elif ( opc == 2 ):
        editTaskDecorator()
        todos.editTask()
        todos.saveDB()

    elif ( opc == 3 ):
        removeTaskDecorator()
        todos.removeTask()
        todos.saveDB()

    else:
        todos.saveDB()
        exit()
#-------------------------------- Apenas Exibem um cabeçalho para a função
def addTaskDecorator(full):
    print("┌┴────────────────────────────────────────────────────────────────────┴┐")
    if (full == "Full"):
        print("│ Não há espaço para novos itens, remova alguns itens                  │")

    else:
        print("│ Adicionar tarefa de no maximo 60 characteres                         │")
    print("└──────────────────────────────────────────────────────────────────────┘")

def editTaskDecorator():
    print("┌┴────────────────────────────────────────────────────────────────────┴┐")
    print("│ Digite o indice da tarefa que deseja editar                          │")
    print("└──────────────────────────────────────────────────────────────────────┘")

def removeTaskDecorator():
    print("┌┴────────────────────────────────────────────────────────────────────┴┐")
    print("│ Digite o indice da tarefa que deseja remover                         │")
    print("└──────────────────────────────────────────────────────────────────────┘")
#--------------------------------

def sort(): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
