import Intepreter

demo1 = "if test"
demo2 = "10 if test"

state = Intepreter.initialize()
Intepreter.interpret(demo1,state)
Intepreter.interpret(demo2,state)
