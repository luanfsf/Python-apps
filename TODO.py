#!/usr/bin/env python3
# encoding: utf-8

def main():
    '''
        Pseudocodigo

        iniciar e ler a lista principal
        exibir status 0 a 100
        exibir a lista principal
        exibir menu de acoes
        newtask
        editTask
        removeTask
'''
class lista:
    
    def __init__(self, ):
        self.lista = readDB()

def readDB():
    ''' Ler o arquivo e para cada linha, ler tarefa e prioridade
    '''
    todolist = []
    with open('todos.db') as db:
        for line in db:
            todolist.append(line.strip().split(';'))


    '''
    # Para ver itens por linha
    for i in range(len(todolist)):
        for j in range(len(todolist[i])):
            print(todolist[i][j] , end=",") # [i][j]
            print(len(todolist[i][j]), end="/")
        print("")
    #print(len(todolist[0])) # Para ver numero de linhas (i)
    #print(len(todolist[0])) # Para ver numero de itens em cada linha (j)
    '''
    return todolist

def saveDB():
    pass

def header():
    print("┌──────────┬──────────────────────────────────────────────────────────┐")
    print("│  TODOs   │                   used 1 of 100                          │")
    print("├──────────┘                                                          │")
    print("├─────────────────────────────────────────────────────────────────────┤")

def formatTasks():
    pass
    # UNIX  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
    # DOS   (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
    # DOS 2 (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )
    ''' ╔══════╗
        ║    ╔═╬═══╦═══╗
        ║    ╚═╩═══╝   ║
        ╚══════════════╝     '''
        
    print("├─────┬───────────────────────────────────────────────────────────────┤")
    print("│ 001 │ Comprar tal coisa                                             │")
    print("├─────┼───────────────────────────────────────────────────────────────┤")
    print("│ 002 │ Comprar tal coisa                                             │")
    print("├─────┼───────────────────────────────────────────────────────────────┤")
    print("│ 003 │ Comprar tal coisa                                             │")
    print("├─────┴───────────────────────────────────────────────────────────────┤")

def endPrompt(): # end of line menu
    print("├─────────────────────────────────────────────────────────────────────┤")
    print("│   1 Nova tarefa |  2 Editar tarefa |  3 Excluir tarefa  |  4 Sair   │")
    print("└─────────────────────────────────────────────────────────────────────┘")
def sortpriority():
    pass
def addTask():
    passs
    class task ():
        pass
    # MAXIMUM TASKS 999
    # PRIORITY (RED,GREEN, YELLOW)
    # NUM-PRIORITY-111111111111111111111111111111111111111111111111111111111111
    # max 70 characteres
    def editTask():
def removeTask():
    
    
if __name__ == '__main__':
	main()
