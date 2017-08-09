#!/usr/bin/python
import Intepreter
import Tokenizer
import Parser


lines = [
    'PRINT 5+5',
    'IF 5 = 5 THEN PRINT "HELLO"'
]

state = Intepreter.initialize()
for line in lines:
    Intepreter.interpret(line, state)
