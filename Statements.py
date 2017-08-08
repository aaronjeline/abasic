class BaseStatment():
    pass

class PrintStatment(BaseStatment):
    arg = None

class IfStatement(BaseStatment):
    exp = None
    result = None

class Statement():
    statement = None
