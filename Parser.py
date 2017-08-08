from Tokenizer import tokenize
import Tokenizer

class Line():
    statement = None
    num = None

def parseStatement(tokens):



def parseLine(tokens):
    new = Line()
    if type(tokens[0]) == Tokenizer.Number:
        new.num = tokens.pop(0)
    new.statement = parseStatement(tokens)
    return new



def parse(line):
    tokens = tokenize(line)
    parseLine(tokens)