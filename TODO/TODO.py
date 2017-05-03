#!/usr/bin/env python3
# encoding: utf-8

import os # time, sys

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

class lista:
    ''' Classe lista, uma lista e métodos básicos para sua manipulação '''

    def __init__(self):

        self.lista = []

    def readDB(self):
        ''' Lê o arquivo todos.db e separa cada linha como uma tarefa
            cada linha contém uma tarefa e uma prioridade, o separador é "**"    '''

        with open("todos.db", "r") as db:
            for line in db:
                self.lista.append(line.strip().split("**"))
                # utilizando ** e não virgulas, para preservar as virgulas na descrição de tarefas
        return self

    def saveDB(self):
        ''' Salva a lista completa no arquivo todos.db, cada linha contendo uma tarefa e
            sua prioridade, separadas por "**". E deverá ser chamado sempre após uma alteração    '''
        outF = open("todos.db", "w")
        for line in self.lista:
            outF.write("**".join(map(str, line)))
            outF.write("\n")
        outF.close()

    def addTask(self):
        ''' Adicionar elemento na lista desde que não ultrapasse o limite de 100, somente
            para manter uma formatação correta. Exibir mensagem (Não é possível adicionar
            mais tarefas, remova algumas tarefas para continuar), caso len(self.lista) > 100 '''
        if (len(self.lista) < 100 ):
            self.lista.append( [ self.Wrapper(), self.Priority()] )
            pass #return
        else:
            print ("Limite de tarefas atingido, delete algumas tarefas")

    def editTask(self):
        ''' Pede o indice do item da lista que deseja alterar, range(0, len(self.list))
            Exibe o item e pede para inserir novo texto e prioridade, caso
            o campo esteja em branco, não alterar e logo pedir a prioridade '''

        if ( len( self.lista ) == 0 ):
            print('A lista não contem itens')
            return

        print('Digite o número da tarefa que deseja editadar, da/s {} tarefa/s '.format( len( self.lista ) ) )

        indice = int(input())

        while (indice not in range(1, len(self.lista) + 1 ) ):
            print('A tarefa selecionada não existe')
            self.editTask()

        # exibir a tarefa que sera editada
        self.lista[indice - 1] = [ self.Wrapper(), self.Priority()]

        return

    def removeTask(self):
        ''' Pede o indice do item que deseja remover, range(0, len(self.list))
            Exibe o item e pergunta se deseja mesmo excluir   '''

        if ( len( self.lista ) == 0 ):
            print('A lista não contem itens')
            return

        print('Digite o número da tarefa que deseja remover, da/s {} tarefa/s '.format( len( self.lista ) ) )

        indice = int(input())

        while (indice not in range(1, len(self.lista) +1 ) ):
            print('A tarefa selecionada não existe')
            indice = int(input())

        del self.lista[ indice -1 ]

        return

    def Wrapper(self, max=60):
        ''' Input de no máximo max characteres para adicionar a lista '''
        task = input( "Digite a tarefa, 60 caracteres no máximo.")
        while ( len(task) > max ):
            print('A tarefa exede o limite de {} caracteres, conforme abaixo'.format(max))
            print("|**********************************************************|") # 60 CHARACTERES
            task = self.Wrapper()
        return task # <- quando estiver pronto

    def Priority(self):
        ''' Input inteiro [1,2,3] para definir a prioridade das tarefas '''
        prioridades = [1,2,3]
        # Pode exibir o texto da prioridade e em seguida pedir a prioridade
        pri = int(input( "Digite a prioridade | 1 | 2 | 3 | "))
        if pri not in prioridades:
            print('As prioridades são | 1 | 2 | 3 | ')
            pri = self.Priority()
        return pri # <- Retornar a prioridade

    def printDB(self): # Método somente para testes, ver itens por linha e len()
        for i in range(len(self.lista)):
            for j in range(len(self.lista[i])):
                print(self.lista[i][j] , end=",")
                print('len = '+ str( len(self.lista[i][j]) ), end="**")
            print("")
        # for i in self.lista:
        #     print(i, end="**" )
        return

# para testes
#a=lista()
#a.saveDB()

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

def COL(opc):
    ''' COL( opc ), retorna string com padrão ANSI para formatação
    opc = string -> ["BLACK", "RED", "GREEN", "YELLOW","BLUE", "MAGENTA", "CYAN" ] '''

    cores = {
    "BLACK"   : "\u001B[30m",
    "RED"     : "\u001B[31m",
    "GREEN"   : "\u001B[32m",
    "YELLOW"  : "\u001B[33m",
    "BLUE"    : "\u001B[34m",
    "MAGENTA" : "\u001B[35m",
    "CYAN"    : "\u001B[36m"
    }
    return cores[opc]

def BCK(opc):
    ''' BCK( opc ), retorna string com padrão ANSI para formatação
    opc = string -> ["BLACK", "RED", "GREEN", "YELLOW","BLUE", "MAGENTA", "CYAN" ] '''

    fundos = {
    "BLACK"   : "\u001B[40m",
    "RED"     : "\u001B[41m",
    "GREEN"   : "\u001B[42m",
    "YELLOW"  : "\u001B[43m",
    "BLUE"    : "\u001B[44m",
    "MAGENTA" : "\u001B[45m",
    "CYAN"    : "\u001B[46m"
    }
    return fundos[opc]

def BLD(): return "\u001B[1m"
def RST(): return "\u001B[0m"
#--------------------------

if __name__ == '__main__':
	main()
