import Parser
import Statements as statements
import Tokenzier as tokens

class State():
    def __init__(self):
        self.variables = {}
        self.lines = [0] * 1000
        self.stack = []


def initialize():
    return State();

def interpretExpression(expression):
    stack = []
    for i in expression:
        if type(i) == t.Number:
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            if i.op == '+':
                stack.append(a+b)
            elif i.op == '-':
                stack.append(a-b)
            elif i.op == '=':
                stack.append(a==b)
            elif i.op == '*':
                stack.append(a*b)
            elif i.op == '/':
                stack.append(a/b)
            elif i.op == '<':
                stack.append(a<b)
            elif i.op == '>':
                stack.append(a>b)
    if len(stack) > 1:
        throw Error()
    return stack[0]


def interpretPrintStatement(statement):
    total = ""
    for i in statement.arg.contents:
        if type(i) == tokens.String:
            total += String.string
        elif:
            total += str(interpretExpression(i))


def interpretStatement(statement):
    if type(statement) == statements.PrintStatement:
        interpretPrintStatement(statement)


def interpret(line, state):
    objects = Parser.parse(line)
    interpretStatement(objects[0])
