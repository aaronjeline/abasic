#!/usr/bin/python
import Intepreter
import Tokenizer
import Parser


lines = [
    'PRINT "hello"',
    'IF 5 = 5 THEN PRINT "HELLO"'
]

state = Intepreter.initialize()
for line in lines:
    print(Parser.parse(line)))
