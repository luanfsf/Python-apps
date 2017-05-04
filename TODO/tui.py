# UNIX-dos  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
# DOS only  (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )

from ansi_easy import *

def header():
    print("┌───────┬────────────────────────────────────────────────────┬─────────┐")
    print("│ TODOs │                                                    │ {3}/100 │")
    print("└┬──────┴────────────────────────────────────────────────────┴────────┬┘")

def showTasks(todos):
    ''' Loop para exibir tarefas '''
    print("┌┴──────┬─────────────────────────────────────────────────────────────┴┐")
    for i in range(len(todos.lista)):
        print("│  {:^3}  │ {:^60} │".format( i+1, todos.lista[i][0]) ) # Incluir formatacao e cor da prioridade
        if (i == len(todos.lista) -1 ):
            print("└┬──────┴─────────────────────────────────────────────────────────────┬┘")
        else:
            print("├───────┼──────────────────────────────────────────────────────────────┤")
    #print("├───────┴──────────────────────────────────────────────────────────────┤")

def endPrompt(): # Chama as funcoes da classe lista, mas não faz parte da classe lista
    print("┌┴────────────────┬──────────────────┬────────────────────┬───────────┴┐")
    print("│  1 Nova tarefa  │  2 Editar tarefa │  3 Excluir tarefa  │   4 Sair   │")
    print("└─────────────────┴──────────────────┴────────────────────┴────────────┘")

    opcoes = [1,2,3,4]
    opc = 0

    while( opc not in opcoes ):
        opc = int(input())

    if ( opc == 1 ):
        todos.addTask()
        todos.saveDB()

    elif ( opc == 2 ):
        todos.editTask()
        todos.saveDB()

    elif ( opc == 3 ):
        todos.removeTask()
        todos.saveDB()

    else:
        todos.saveDB()
        exit()

def sort(): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
