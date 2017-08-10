import Tokenizer as t
from Tokenizer import tokenize
import Statements

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
    if cur != []:
        new.contents.append(parseExpression(cur))
    return new

def parsePrintStatement(tokens):
    #first token is keyword
    #Rest is an expr-list
    new = Statements.PrintStatement()
    new.arg = parseExprList(tokens[1:])
    return new

def parseIfStatement(tokens):
    new = Statements.IfStatement()
    #Find the THEN keyword.
    expBound = None
    for token in tokens[1:]:
        if type(token) == t.Keyword and token.keyword == 'THEN':
            expBound = tokens[1:].index(token)
    if expBound is None:
        raise Exception('Expected THIS before newline')
    new.exp = parseExpression(tokens[1:expBound+1])
    new.result = parseStatement(tokens[expBound+2:])
    return new

def parseGotoStatement(tokens):
    new = Statements.GotoStatement()
    new.exp = parseExpression(tokens[1:])
    return new

def parseLetStatement(tokens):
    new = Statements.LetStatement()
    if type(tokens[1]) == t.Identifier:
        new.var = tokens[1].i
    else:
        raise Exception('Expected Identifier as 2nd token in LET statement')
    if type(tokens[2]) != t.Operator and tokens[2].op != '=':
        raise Exception('Expected "=" before expression in LET statement')
    new.val = parseExpression(tokens[3:])
    return new

def parseGoSubStatement(tokens):
    new = Statements.GoSubStatement()
    new.dest = parseExpression(tokens[1:])
    return new

def parseStatement(tokens):
    new = None
    if type(tokens[0]) != t.Keyword:
        raise Exception('Statement Doesn\'t begin with a keyword.')
    elif tokens[0].keyword == 'PRINT':
        new = parsePrintStatement(tokens)
    elif tokens[0].keyword == 'IF':
        new = parseIfStatement(tokens)
    elif tokens[0].keyword == 'RUN':
        new = Statements.RunStatement()
    elif tokens[0].keyword == 'END':
        new = Statements.EndStatement()
    elif tokens[0].keyword == 'GOTO':
        new = parseGotoStatement(tokens)
    elif tokens[0].keyword == 'LET':
        new = parseLetStatement(tokens)
    elif tokens[0].keyword == 'GOSUB':
        new = parseGoSubStatement(tokens)
    elif tokens[0].keyword == 'RETURN':
        new = Statements.ReturnStatement()
    else:
        raise Exception('Unknown Keyword')
    return new




def parseLine(tokens):
    new = Line()
    if type(tokens[0]) == t.Number:
        new.num = tokens.pop(0).value
    new.statement = parseStatement(tokens)
    return new



def parse(line):
    tokens = tokenize(line)
    return parseLine(tokens)
