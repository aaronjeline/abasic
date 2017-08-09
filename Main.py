#!/usr/bin/python
import Intepreter
import Tokenizer
import Parser


lines = [
    '10 PRINT 5!5+5-4*,"hello"',
    '20 IF 5!1+6= THEN GOTO 40',
    '30 GOTO 50',
    '40 PRINT "GOTO\'d"',
    '50 END',
    'RUN'
]

state = Intepreter.initialize()
for line in lines:
    Intepreter.interpret(line, state)
