#!/usr/bin/python
import Intepreter
import Tokenizer
import Parser


lines = [
    'LET x = 5!5+',
    'PRINT x'
]

state = Intepreter.initialize()
for line in lines:
    Intepreter.interpret(line, state)
