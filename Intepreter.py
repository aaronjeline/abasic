import Parser
import Statements as statements
import Tokenizer as tokens

class State():
    def __init__(self):
        self.variables = {}
        self.lines = [0] * 1000
        self.stack = []
        self.pc = 0
        self.halt = True


def initialize():
    return State();

def interpretExpression(expression, state):
    stack = []
    for i in expression.contents:
        if type(i) == tokens.Number:
            stack.append(i.value)
        else:
            b = stack.pop()
            a = stack.pop()
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
        raise Exception('Non singular stack left over!')
    return stack[0]


def interpretPrintStatement(statement, state):
    total = ""
    for i in statement.arg.contents:
        if type(i) == tokens.String:
            total += i.string
        else:
            total += str(interpretExpression(i,state))
    print(total)

def interpretIfStatement(statement, state):
    boolean = interpretExpression(statement.exp, state)
    if boolean:
        interpretStatement(statement.result, state)

def interpretRunStatement(state):
    state.halt = False
    try:
        while not state.halt:
            cur = state.pc
            state.pc += 1
            curInsturction = state.lines[cur]
            #Don't process NOPs or RUNS
            if curInsturction == 0 or type(curInsturction) == statements.RunStatement:
                pass
            else:
                interpretStatement(curInsturction,state)
    except IndexError:
        print('Reached end of line space, halting!')

def interpretEndStatement(state):
    state.halt = True


def interpretStatement(statement, state):
    if type(statement) == statements.PrintStatement:
        interpretPrintStatement(statement, state)
    elif type(statement) == statements.IfStatement:
        interpretIfStatement(statement, state)
    elif type(statement) == statements.RunStatement:
        interpretRunStatement(state)
    elif type(statement) == statements.EndStatement:
        interpretEndStatement(state)


def interpret(line, state):
    objects = Parser.parse(line)
    if objects.num is not None:
        try:
            state.lines[objects.num] = objects.statement
        except ValueError:
            print('Invalid Line Number!')
    else:
        interpretStatement(objects.statement, state)
