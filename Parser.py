class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'NUMBER(' + str(self.value) + ')'

def safeIntCast(c):
    try:
        val = int(c)
        return True
    except ValueError:
        return False

# digit digit*
def parseNumber(piece):
    if(all(map(safeIntCast, piece))):
        return Number(int(piece))
    else:
        return False

class Statement():
    def __init__(self, command, args=None):
        self.command = command
        self.args = args

    def __str__(self):
        return 'STATEMENT("' + self.text + '")'


def parseStatement(statement):
    command = statement.pop(0)
    args = {}
    if command == 'PRINT':
        args['EXPR-LIST'] = statement[0]
        return Statement(command,args)
    elif command == 'IF':
        args['EXP1'] = statement[0]
        args['RELOP'] = statement[1]
        args['EXP2'] = statement[3]
        args['THEN'] = statement[4]
        args['RESULT'] = parseStatement(statement[5])
        return Statement(command.args)
    elif command == 'GOTO':
        args['EXPR'] = statement[0]
        return Statement(command,args)
    elif command == 'INPUT':
        args['VAR_LIST'] = statement[0]
        return Statement(command,args)
    elif command == 'LET':
        args['VAR'] = statement[0]
        args['='] = statement[1]
        args['EXPR'] = statement[2]
        return Statement(command,args)
    elif command == 'GOSUB':
        args['EXPR'] = statement[0]
        return Statement(command.args)
    elif command == 'RETURN':
        return Statement(command)
    elif command == 'CLEAR':
        return Statement(command)
    elif command == 'LIST':
        return Statement(command)
    elif command == 'RUN':
        return Statement(command)
    elif command == 'END':
        return Statement(command)
    else:
        return False






# number statement CR | statement CR
def parseLine(text):
    pieces = text.split(' ')
    results = []
    if(parseNumber(pieces[0])):
        results.append(parseNumber(pieces[0]))
        pieces.pop(0)
    results.append(parseStatement(pieces[0:]))
    return results







def parse(line):
    pass