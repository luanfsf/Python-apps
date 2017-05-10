class lista:

    ''' Classe lista, uma lista e métodos básicos para sua manipulação '''

    def __init__(self):
        pass

    def readDB(self):

        ''' Lê o arquivo todos.db e separa cada linha como uma tarefa cada
        linha contém uma tarefa e uma prioridade, o separador é "**" '''

        self.lista = []

        with open("todos.db", "r") as db:
            [self.lista.append(line.strip().split("**")) for line in db]

        return

    def saveDB(self):

        ''' Salva a lista completa no arquivo todos.db, cada linha contendo
        uma tarefa e sua prioridade, separadas por "**". E deverá ser chamado
        sempre após uma alteração '''

        with open("todos.db", "w") as outF:
            for line in self.lista:
                outF.write("**".join(map(str, line)))
                outF.write("\n")

        return

    def addTask(self):

        ''' Adicionar elemento na lista desde que não ultrapasse o limite de
            60 caracteres somente para manter uma formatação correta. '''

        self.lista.append( [ self.Wrapper(), self.Priority()] )

    def Wrapper(self, max=60):

        ''' Input de no máximo max characteres para adicionar a lista '''

        task = input( )

        if ( len(task) > max ):
            task = self.Wrapper()

        return task

    def Priority(self):

        ''' Input inteiro [1,2,3] para definir a prioridade das tarefas '''

        prioridades = [1,2,3]
        
        pri = int(input())

        if ( pri not in prioridades):
            pri = self.Priority()

        return pri

    def editTask(self, indice):

        ''' Editar a tarefa no indice selecionado '''

        self.lista[ indice - 1] = [ self.Wrapper(), self.Priority()]

        return

    def removeTask(self, indice):

        ''' Pede o indice do item que deseja remover, range(0, len(self.list))
        Exibe o item e pergunta se deseja mesmo excluir   '''

        del self.lista[ indice -1 ]

        return

    def checkindex(self, indice):

        ''' Verifica se o indice desejado faz parte da lista, retorna 0 caso
        não faça parte do indice, caso contrário retorna o indice '''

        if (indice not in range(1, len(self.lista) + 1 ) ):
            return 0

        return indice

    def checklen(self):

        ''' Retorna 1 se a lista contém menos de 100 itens, 0 caso contrário '''

        if (len(self.lista) < 100 ):
            return 1

        return 0

    def checkempty(self):

        ''' Retorna 1 caso a lista não contenha itens, 0 caso contrário'''

        if ( len( self.lista ) == 0 ):
            return 1

        return 0

    def printDB(self): # Método somente para testes, ver itens por linha e len()
        for i in range(len(self.lista)):
            for j in range(len(self.lista[i])):
                print(self.lista[i][j] , end=",")
                print('len = '+ str( len(self.lista[i][j]) ), end="**")
            print("")
        return
