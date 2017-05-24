'''Classe lista, uma lista e métodos básicos para sua manipulação.
'''

class Lista:

    def __init__(self):
        pass

    def readDB(self):
        '''Lê o arquivo todos.db e adiciona cada tupla como uma tarefa em,
        uma lista cada linha contém uma tarefa e uma prioridade, o separador
        utilizado é "**".
        '''

        self.lista = []

        with open("todos.db", "r") as db:
            [self.lista.append(line.strip().split("**")) for line in db]

        return

    def saveDB(self):
        '''Salva a lista completa no arquivo todos.db, cada linha contendo
        uma tarefa e sua prioridade, separadas por "**". E deverá ser chamado
        sempre após uma alteração.
        '''

        with open("todos.db", "w") as outF:
            for line in self.lista:
                outF.write("**".join(map(str, line)))
                outF.write("\n")

        return

    def addTask(self):
        '''Cria uma tupla contendo uma tarefa e sua respectiva prioridade,
        os sequintes métodos da própria classeserão chamados para realizar
        essa tarefa: self.Wrapper() e self.Priority() .
        '''

        self.lista.append( [ self.Wrapper(), self.Priority()] )

    def Wrapper(self, max=60):
        '''Função que irá pedir a tarefa, caso a mensagem ultrapasse o máximo
        max de characteres ou nada tenha sido digitado, a função self.Wrapper()
        será novamente invocada.
        '''

        task = input( )

        if ( (len(task) > max) or (task == "" ) ):
            task = self.Wrapper()

        return task

    def Priority(self):
        '''Função que iŕa pedir um inteiro emtre 1 e 3 para definir a
        prioridade da respectiva tarefa.
        '''

        prioridades = range(1,4)

        pri = int(input())

        if ( pri not in prioridades):
            pri = self.Priority()

        return pri

    def editTask(self, indice):
        '''Editar a tarefa no indice selecionado.
        '''

        self.lista[ indice - 1] = [ self.Wrapper(), self.Priority()]

        return

    def removeTask(self, indice):
        '''Remove o item no indice que desejado.
        '''

        del self.lista[ indice -1 ]

        return

    def checkindex(self, indice):
        '''Verifica se o indice desejado faz parte da lista, retorna 0 caso
        não faça parte do indice, caso contrário retorna o indice.
        '''

        if (indice not in range(1, len(self.lista) + 1 ) ):
            return 0

        return indice

    def checklen(self):
        '''Retorna 1 se a lista contém menos de 100 itens, 0 caso contrário.
        '''

        if (len(self.lista) < 100 ):
            return 1

        return 0

    def checkempty(self):
        '''Retorna 1 caso a lista não contenha itens, 0 caso contrário
        '''

        if ( len( self.lista ) == 0 ):
            return 1

        return 0
