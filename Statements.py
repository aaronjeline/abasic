class BaseStatment():
    pass

class PrintStatement(BaseStatment):
    arg = None

class IfStatement(BaseStatment):
    exp = None
    result = None

class Statement():
    statement = None
