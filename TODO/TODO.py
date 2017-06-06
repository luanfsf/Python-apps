#!/usr/bin/env python3
# encoding: utf-8

import lista_class as LC, tui as UI

def main():
    '''                      Pseudocodigo
    Instanciar classe lista

    Ler o arquivo todos.db e adicionar linhas a lista da instancia

    Exibir a barra de uso e a lista principal
    Exibir menu de acoes (acoes sao metodos da classe lista, exceto sair)
    Executar tarefas do prompt

    Salvar lista '''

    Todos = LC.Lista()

    while True:
        Todos.readDB()

        UI.clear()
        UI.header( len(Todos.lista) )
        UI.showTasks(Todos)
        UI.endPrompt(Todos)

        Todos.saveDB()

if __name__ == '__main__':
	main()
