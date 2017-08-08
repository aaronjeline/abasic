import Tokenizer as t
from t import tokenize

class Line():
    statement = None
    num = None

class ExprList():
    def __init__(self):
        self.contents = []

class Expression():
    def __init__(self):
        self.contents = []

def parseExpression(tokens):
    new = Expression()
    for i in tokens:
        if type(i) != t.Seperator:
            new.contents.append(i)
    return new


def parseExprList(tokens):
    new = ExprList()
    cur = []
    for token in tokens:
        if type(token) == t.String:
            new.contents.append(token)
        elif type(token) == t.Comma:
            if cur != []:
                new.contents.append(parseExpression(cur))
                cur = []
        else:
            cur.append(token)
    return new

def parsePrintStatement(tokens):
    #first token is keyword
    #Rest is an expr-list
    new = PrintStatement()
    new.arg = parseExprList(tokens[1:])
    return new



def parseStatement(tokens):
    new = Statement()
    if type(tokens[0]) != t.Keyword:
        throw Error
    elif tokens[0].keyword == 'PRINT':
        Statement.statment = parsePrintStatement(tokens)




def parseLine(tokens):
    new = Line()
    if type(tokens[0]) == t.Number:
        new.num = tokens.pop(0)
    new.statement = parseStatement(tokens)
    return new



def parse(line):
    tokens = tokenize(line)
    parseLine(tokens)
