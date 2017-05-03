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
