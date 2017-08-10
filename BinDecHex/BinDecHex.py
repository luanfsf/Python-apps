#!/usr/bin/python3
import sys # Somente para aceitar argumentos para os testes

def main():
    '''
    Cada função, deve ser chamada, inicialmente, somente com um valor inteiro,
    pois assim a lista começará a será utilizada como arguento para as chamadas
    recursivas, acumulando os caracteres, em seguida a função verifica se o
    inteiro é igual a zero, se sim, nesse caso ele inverte a ordem da lista,
    concatena os valores e retorna uma string com os valores, caso contrário,
    continua a adicionar o caractere correspondente ao restante do operador
    módulo, 0 e 1 na função binária e na função hexadecimal utilizando o
    dicionário hexTable, em seguida subtrai o restante do operador módulo do
    valor inteiro, então chama novamente a prória função, mas passa como
    argumento o valor inteiro dividido pela base correspondente, já que a sobra
    ja foi subtraida, também passa a lista como argumento, pois o caractere
    necessário já foi adicionado na chamada atual.

    No programa tem uma função para testes, que compara as strings retornadas
    pela minha função com as strings retornadas pelas funções nativas do python
    bin() e hex()
    '''
    inteiro = int(input("Digite um numero inteiro, para ver o valor binário e hexadecimal: "))
    print("O valor binário é: {}".format( decToBin(inteiro) ) )
    print("O valor hexadecimal é: {}".format( decToHex(inteiro) ) )

def decToBin(inteiro, lista=None):

    # Inicia lista caso o parâmetro lista não tenha valor
    if (lista == None):
        lista = []

    # Caso o inteiro seja igual a zero, é melhor entregar tudo, pois não há
    # mais nada a fazer
    if inteiro == 0:

        # inverte a lista
        lista.reverse()

        # Caso especial para quando o valor é 0
        if (len(lista ) == 0):
            return('0')

        # Concatena a lista e retorna o valor no formato string
        return "".join( [str(x) for x in lista] )

    # Adiciona o restante à lista, 0 ou 1
    lista.append( str(int(inteiro % 2) ) )

    # Remove o restante do inteiro atual, eu sei que 0 em alguns casos
    inteiro -= inteiro % 2

    # O retorno vai depender de mais uma chamada, agora com o inteiro dividido
    # pela base, nesse caso 2, e a lista vai como argumento, mas não por valor
    # mas como um objeto mutavel que aqui nessa função tem o mesmo endereço
    return decToBin(inteiro/2, lista)

def decToHex(inteiro, lista=None):

    # Inicia lista caso o parâmetro lista não tenha valor
    if (lista == None):
        lista = []

    # Caso o inteiro seja igual a zero, é melhor entregar tudo, pois não há
    # mais nada a fazer
    if inteiro == 0:
        # inverte a lista
        lista.reverse()

        if (len(lista ) == 0):
            # Caso especial para quando o valor é 0
            return('0')

        # Concatena a lista e retorna o valor no formato string
        return "".join([str(x) for x in lista])

    # Adiciona o restante à lista, utilizando o dicionário hexTable
    lista.append( hexTable[ str( int( inteiro % 16 ) ) ] if (inteiro % 16 > 9 ) else str(int(inteiro%16)) )

    # Remove o restante do inteiro atual, eu sei que 0 em alguns casos
    inteiro -= inteiro % 16

    # O retorno vai depender de mais uma chamada, agora com o inteiro dividido
    # pela base, nesse caso 16, e a lista vai como argumento, mas não por valor
    # mas como um objeto mutavel que aqui nessa função tem o mesmo endereço
    return decToHex(inteiro/16, lista)

def testes(N):
    '''Para testar se as funções estão retornando o valor certo, os testes
    apenas comparam as strings retornadas pelas funções nativas do python
    bin() e hex() com as string retornadas pelas minhas funções decToBin() e
    decToHex() e caso os resultados sejam diferentes, um erro será adicionado
    a um acumulador de errors para a respectiva função. '''

    BinError = 0
    HexError = 0

    for i in range(N):
        # print("{} = {}  |".format(bin(i)[2:], decToBin(i)), end= "")
        # print(" {} | {}".format(hex(i)[2:], decToHex(i)))
        if ( bin(i)[2:] != decToBin(i) ):
            BinError += 1
        elif ( hex(i)[2:] != decToHex(i) ):
            HexError += 1

    print("Função decToBin: {} erros em {} testes".format(BinError, N))
    print("Função decToHex: {} erros em {} testes".format(HexError, N))

if __name__ == "__main__":

    hexTable = {
    # Dicionário de valores correspondentes de decimal para hexadecimal.
    # Esse dicionário está dentro do namespace desse programa e será utilizado
    # pela função decToHex
    "10":"a", "11":"b", "12":"c",
    "13":"d", "14":"e", "15":"f"
    }

    # Para realizar testes, $python BinDecHex.py teste N, onde N é o número de testes
    # para seren realizados, iniciando com o valor 0
    if (len(sys.argv) > 1):
        if (sys.argv[1] == 'teste' and int(sys.argv[2]) > 0):
            testes(int(sys.argv[2]))
            exit()

    main()
