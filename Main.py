#!/usr/bin/python
import Intepreter
import Tokenizer
import Parser


lines = [
    '1 PRINT "START"',
    '2 GOSUB 5',
    '3 PRINT "AFTER_SUB"',
    '4 END',
    '5 PRINT "SUB"',
    '6 RETURN',
    'RUN'
]

state = Intepreter.initialize()
for line in lines:
    Intepreter.interpret(line, state)
