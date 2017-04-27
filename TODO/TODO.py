#!/usr/bin/env python3
# encoding: utf-8

def main():
    ''' Pseudocodigo

    Ler e instanciar lista principal

    exibir status 0 a 100
    exibir a lista principal
    exibir menu de acoes (acoes sao metodos da classe lista)
    '''

    Todos = lista()

    while True:
        header(Todos.lista)
        showTasks(Todos.lista)
        if ( endPrompt (Todos) == False):
            break

class lista:
    ''' Classe lista irá conter uma lista e métodos básicos para sua manipulação
    '''

    def __init__(self):
        self.lista = self.readDB()

    def readDB(self):
        ''' Lê o arquivo todos.db e separa cada linha como uma tarefa
            cada linha contém uma tarefa e uma prioridade, o separador é "**"    '''
        todos = []
        with open("todos.db", "r") as db:
            for line in db:
                todos.append(line.strip().split("**"))
                # utilizando ** e não virgulas, para preservar as virgulas na descrição de tarefas
        return todos

    def saveDB(self):
        ''' Salva a lista completa no arquivo todos.db, cada linha contendo uma tarefa e
            sua prioridade, separadas por "**". E deverá ser chamado sempre após uma alteração    '''
        outF = open("todos2.db", "w")
        for line in self.lista:
            outF.write("**".join(map(str, line)))
            outF.write("\n")
        outF.close()

    def addTask(self):
        ''' Adicionar elemento na lista desde que não ultrapasse o limite de 100, somente
            para manter uma formatação correta. Exibir mensagem (Não é possível adicionar
            mais tarefas, remova algumas tarefas para continuar), caso len(self.lista) > 100 '''
        if (len(self.list) < 100 ):
            self.list.append( [ Wrapper(), Priority()] )
            pass #return
        print ("Limite de tarefas atingido, delete algumas tarefas")

        def Wrapper(max=60):
            ''' Input de no máximo max characteres para adicionar a lista '''
            print("|**********************************************************|") # 60 CHARACTERES
            task = input( "{}{}Digite a tarefa, 60 caracteres no máximo.{}".format(BLD(),COL("BLUE"),RST()) )
            if ( len(task) > max ):
                print('A tarefa exede o limite de {} caracteres'.format(max))
                Wrapper()
            return task # <- quando estiver pronto
        def Priority():
            ''' Input inteiro [1,2,3] para definir a prioridade das tarefas '''
            prioridades = [1,2,3]
            # Pode exibir o texto da prioridade e em seguida pedir a prioridade
            pri = input( "Digite a prioridade | 1 | 2 | 3 | " )
            while pri not in prioridades:
                print('As prioridades são | 1 | 2 | 3 | ')
                Priority()
            return pri # <- Retornar a prioridade

        return

    def editTask(self):
        ''' Pede o indice do item da lista que deseja alterar, range(0, len(self.list))
            Exibe o item e pede para inserir novo texto e prioridade, caso
            o campo esteja em branco, não alterar e logo pedir a prioridade
        '''
        pass

    def removeTask(self):
        ''' Pede o indice do item que deseja remover, range(0, len(self.list))
            Exibe o item e pergunta se deseja mesmo excluir
        '''
        pass

    def printDB(self): # Método somente para testes, ver itens por linha e len()
        for i in range(len(self.lista)):
            for j in range(len(self.lista[i])):
                print(self.lista[i][j] , end=",")
                print('len = '+ str( len(self.lista[i][j]) ), end="**")
            print("")
        # for i in self.lista:
        #     print(i, end="**" )
        return

# para testes
a=lista()
a.saveDB()

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
    print("├─────┼──────────────────────────────────────────────────────────────┤")
    print("│ 003 │ Comprar tal coisa                                            │")
    print("├─────┴──────────────────────────────────────────────────────────────┤")

def endPrompt(todos): # end of line menu
    print("├────────────────────────────────────────────────────────────────────┤")
    print("│  1 Nova tarefa  |  2 Editar tarefa |  3 Excluir tarefa  |  4 Sair  │")
    print("└────────────────────────────────────────────────────────────────────┘")
    opcoes = [1,2,3,4]
    opc = 0
    while( opc not in opcoes ):
        opc = int(input())
    return False

def sort(): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    pass


def COL(opc):
    ''' COL( opc ), retorna string com padrão ANSI para formatação
    opc = string -> ["BLACK", "RED", "GREEN", "YELLOW","BLUE", "MAGENTA", "CYAN" ]
    '''
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
    opc = string -> ["BLACK", "RED", "GREEN", "YELLOW","BLUE", "MAGENTA", "CYAN" ]
    '''
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
