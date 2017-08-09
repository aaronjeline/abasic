#!/usr/bin/python
import Intepreter
import Tokenizer
import Parser


lines = [
    'PRINT 5!5+5-4*,"hello"',
    'IF 55= THEN PRINT "HELLO"'
]

state = Intepreter.initialize()
for line in lines:
    Intepreter.interpret(line, state)
