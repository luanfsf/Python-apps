#!/usr/bin/env python3
# encoding: utf-8

import os # time, sys

from lista_class import lista
from ansi_easy import *
from tui import *

def main():
    '''                      Pseudocodigo
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

if __name__ == '__main__':
	main()
