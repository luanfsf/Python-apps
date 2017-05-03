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
        todos.saveDB()
        exit()

def sort(): # fazer mais tarde, ordenar por prioridade, nao alterar a ordem da lista original
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
