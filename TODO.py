#!/usr/bin/env python3
# encoding: utf-8

def main():
#    ''' Pseudocodigo
#
#        iniciar e ler a lista principal
#        
#        exibir status 0 a 100
#        exibir a lista principal
#        exibir menu de acoes
#    '''
#    TODOS = lista
#    
#    while True:
#        header    (TODOS)
#        showTasks (TODOS)
#        endPrompt (TODOS)
#    
    
    class lista:
            
        def readDB(self):
            todos = []
            with open('todos.db') as db:
                for line in db:
                    todos.append(line.strip().split(','))
            return todos
        
        def __init__(self):
            self.lista = self.readDB()
            #self.size = self.len(self.lista)
    
        def printDB(self):
            for i in range(len(self.lista)): # Para ver itens por linha e len()
                for j in range(len(self.lista[i])):
                    print(self.lista[i][j] , end=",") # [i][j]
                    print('len = '+ str( len(self.lista[i][j]) ), end="/")
                print("")
    
        def saveDB(self):
            
            outF = open("todos2.db", "w")
            for line in self.lista:
                #outF.write(str(line)+"")
                outF.write(str(line).replace("[","").replace("]", "").replace(" '", "").replace("'", ""))
                outF.write("\n")
            outF.close()
            # salvar cada elemento da lista no arquivo
#        def addTask(self):
#            # Adicionar elemento na lista desde que não ultrapasse o limite de 100, exibir mensagem
#            pass
#        def editTask(self):
#            #self.list.append()
#            pass
#        def removeTask(self):
#            pass
    a=lista()
    a.saveDB()
    
    def header():
        print("┌──────────┬─────────────────────────────────────────────────┬───────┐")
        print("│  TODOs   │                                                 │ 1/100 │")
        print("├──────────┴─────────────────────────────────────────────────┴───────┤")
    
    def showTasks(TODO):
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
    
#    def endPrompt(): # end of line menu
#        print("├────────────────────────────────────────────────────────────────────┤")
#        print("│  1 Nova tarefa  |  2 Editar tarefa |  3 Excluir tarefa  |  4 Sair  │")
#        print("└────────────────────────────────────────────────────────────────────┘")
#        
#        opc = 0
#        while( opc != 4):
#            return True

    #-------------------------CORES
    BLACK       = "\u001B[30m"
    RED         = "\u001B[31m"
    GREEN       = "\u001B[32m"
    YELLOW      = "\u001B[33m"
    BLUE        = "\u001B[34m"
    MAGENTA     = "\u001B[35m"
    CYAN        = "\u001B[36m"
    #------------------------FUNDOS    
    BCK_BLACK   = "\u001B[40m"
    BCK_RED     = "\u001B[41m"
    BCK_GREEN   = "\u001B[42m"
    BCK_YELLOW  = "\u001B[43m"
    BCK_BLUE    = "\u001B[44m"
    BCK_MAGENTA = "\u001B[45m"
    BCK_CYAN    = "\u001B[46m"
    BCK_DEFAULT = "\u001B[49m"
    #------------------------OUTROS
    BOLD        = "\033[1m"
    BOLD1       = "\u001B[1m"
    BOLD2       = "\e[1m"
    RESET       = "\u001B[0m"
    #--------------------------
    
#    def sort(): # fazer mais tarde, nao alterar a lista original
#        pass
    
if __name__ == '__main__':
	main()