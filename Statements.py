class BaseStatment():
    pass

class PrintStatment(BaseStatment):
    arg = None

class IfStatement(BaseStatment):
    exp1 = None
    relop = None
    exp2 = None
    result = None

class Statement():
    statement = None
