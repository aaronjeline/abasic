#!/usr/bin/python
import Intepreter
import Tokenizer
import Parser


lines = [
    '10 PRINT 5!5+5-4*,"hello"',
    '20 IF 5!1+6= THEN PRINT "HELLO"',
    '30 END',
    'RUN'
]

state = Intepreter.initialize()
for line in lines:
    Intepreter.interpret(line, state)
