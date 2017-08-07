import Intepreter


lines = [
    'PRINT "hello"',
    'IF '
]

state = Intepreter.initialize()
Intepreter.interpret(demo1,state)
Intepreter.interpret(demo2,state)
