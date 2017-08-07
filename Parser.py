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
        args['EXPR-LIST'] = sum(statement)
        return Statement(command,args)
    elif command == 'IF':
        args['EXP1'] = statement[0]
        args['RELOP'] = statement[1]
        args['EXP2'] = statement[3]
        args['THEN'] = 'THEN'
        args['RESULT'] = parseStatement(statement[5])
        return Statement(command.args)
    elif command == 'GOTO':
        args['EXPR'] = statement[0]
        return Statement(command,args)
    elif command == 'INPUT':
        args['VAR_LIST'] = statem





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