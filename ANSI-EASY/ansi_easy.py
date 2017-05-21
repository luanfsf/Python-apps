''' Simple formatting library, the easy way is to copy and paste it on your project or import it.
'''

def COL(opc):
    '''
    Returns string with ANSI escape sequence respective to the color specified as text color
    COL( opc ), where opc can be one of the following :
    opc = string -> ["BLACK", "RED", "GREEN", "YELLOW","BLUE", "MAGENTA", "CYAN" ]
    e.g. print("{}ALERT!".format(COL("RED"))) '''

    cores = {
    "DEFAULT" :  "\u001B[1m",
    "GRAY"    : "\u001B[30m",
    "RED"     : "\u001B[31m",
    "GREEN"   : "\u001B[32m",
    "YELLOW"  : "\u001B[33m",
    "BLUE"    : "\u001B[34m",
    "MAGENTA" : "\u001B[35m",
    "CYAN"    : "\u001B[36m",
    "LGRAY"   : "\u001B[37m"
    }
    return cores[opc]

def BCK(opc):
    '''
    Returns string with ANSI escape sequence respective to the color specified as background color
    BCK( opc ), where opc can be one of the following :
    opc = string -> ["BLACK", "RED", "GREEN", "YELLOW","BLUE", "MAGENTA", "CYAN", "LGRAY" ]
    e.g. print("{}ALERT!".format(BCK("RED"))) '''

    fundos = {
    "DEFAULT" :  "\u001B[1m",
    "GRAY"    : "\u001B[40m",
    "RED"     : "\u001B[41m",
    "GREEN"   : "\u001B[42m",
    "YELLOW"  : "\u001B[43m",
    "BLUE"    : "\u001B[44m",
    "MAGENTA" : "\u001B[45m",
    "CYAN"    : "\u001B[46m",
    "LGRAY"   : "\u001B[47m"
    }
    return fundos[opc]

def INV():
    ''' Hiddens the text, Not compatible with all terminals '''
    return "\u001B[8m"

def BLD():
    ''' Bold text, Not compatible with all terminals '''
    return "\u001B[1m"

def RST():
    ''' Resets the output to terminal's standard '''
    return "\u001B[0m"
