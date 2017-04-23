#!/usr/bin/env python3
# encoding: utf-8

def main():
    #---------------------MAIN
    Todos = lista()
    
    while True:
        header(Todos)
        showTasks(Todos)
        endPrompt (Todos)
    
    ''' Pseudocodigo

        iniciar e ler a lista principal
        
        exibir status 0 a 100
        exibir a lista principal
        exibir menu de acoes
    '''
    #---------------------MAIN
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
            mais tarefas, remova algumas tarefas para continuar), caso len(Todos.lista) > 100'''
        pass
    def editTask(self):
        #self.list.append()
        pass
    def removeTask(self):
        pass
        
    def printDB(self): # Método somente para testes, ver itens por linha e len()
        for i in range(len(self.lista)): 
            for j in range(len(self.lista[i])):
                print(self.lista[i][j] , end=",") 
                print('len = '+ str( len(self.lista[i][j]) ), end="/")
            print("")
        return

# para testes
a=lista()
a.saveDB()

def header(todos):
    print("┌──────────┬─────────────────────────────────────────────────┬───────┐")
    print("│  TODOs   │                                                 │ 1/100 │")
    print("├──────────┴─────────────────────────────────────────────────┴───────┤")

def showTasks(todos):
    # UNIX  (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
    # DOS   (  ┘ └ ┐ ┌ ┼ ─ ├ ┤ ┴ ┬ │ )
    
    # DOS 2 (  ╝ ╚ ╗ ╔ ╬ ═ ╠ ╣ ╩ ╦ ║ )
    ''' ╔════╗
        ║oi╔═╬══╦══╗
        ║oi╚═╩══╝oi║
        ╚══════════╝     '''
        
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
    
    opc = 0
    while( opc != 4):
        return True

def sort(): # fazer mais tarde, nao alterar a lista original
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