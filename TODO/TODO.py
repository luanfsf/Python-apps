#!/usr/bin/env python3
# encoding: utf-8

import os # time, sys
from lista_class ansi-easy import lista
from ansi_easy import *

def main():
    ''' Pseudocodigo

    Instanciar classe lista

    Ler o arquivo todos.db e adicionar linhas a lista da instancia

    Exibir status 0 a 100
    Exibir a lista principal
    Exibir menu de acoes (acoes sao metodos da classe lista, exceto sair)
    Executar tarefas do prompt
    Salvar lista '''

    Todos = lista()

    while True:
        Todos.readDB()

        clear()
        header(Todos.lista)
        showTasks(Todos.lista)
        endPrompt(Todos)

        Todos.saveDB()

def header(todos):
    print("┌──────────┬─────────────────────────────────────────────────┬───────┐")
    print("│  TODOs   │                                                 │ 1/100 │")
    print("├──────────┴─────────────────────────────────────────────────┴───────┤")

def showTasks(todos):
    # UNIX-dos  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
    # DOS only  (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )

    print("├─────┬──────────────────────────────────────────────────────────────┤")
    print("│ 001 │ Comprar tal coisa                                            │")
    print("├─────┼──────────────────────────────────────────────────────────────┤")
    print("│ 002 │ 1             max character = 60                          60 │")
    print("├─────┴──────────────────────────────────────────────────────────────┤")

def endPrompt(todos): # Chama as funcoes da classe lista, mas não faz parte da classe lista
    print("├─────────────────┬──────────────────┬────────────────────┬──────────┤")
    print("│  1 Nova tarefa  │  2 Editar tarefa │  3 Excluir tarefa  │  4 Sair  │")
    print("└─────────────────┴──────────────────┴────────────────────┴──────────┘")

    opcoes = [1,2,3,4]
    opc = int(input())

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
        exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sort(): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    pass

if __name__ == '__main__':
	main()
