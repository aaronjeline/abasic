import Intepreter
import Tokenizer


lines = [
    'PRINT "hello"',
    'IF 5 = 5 THEN PRINT "HELLO"'
]

state = Intepreter.initialize()
for line in lines:
    print(Tokenizer.tokenize(line))
