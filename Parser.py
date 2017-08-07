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
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'STATEMENT("' + self.text + '")'


def parseStatement(statement):
    return Statement(statement)



# number statement CR | statement CR
def parseLine(text):
    pieces = text.split(' ')
    results = []
    if(parseNumber(pieces[0])):
        results.append(parseNumber(pieces[0]))
        pieces.pop(0)
    results.append(parseStatement(pieces[0]))
    return results







def parse(line):
    pass