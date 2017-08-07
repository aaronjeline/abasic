import Parser

class State():
    def __init__(self):
        self.variables = {}
        self.lines = [0] * 1000
        self.stack = []


def initialize():
    return State();


def interpret(line, state):
    objects = Parser.parseLine(line)
    for i in objects:
        print(i)

