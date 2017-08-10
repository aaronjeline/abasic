class BaseStatment():
    pass

class PrintStatement(BaseStatment):
    arg = None

class IfStatement(BaseStatment):
    exp = None
    result = None

class RunStatement(BaseStatment):
    pass

class EndStatement(BaseStatment):
    pass

class GotoStatement(BaseException):
    exp = None

class LetStatement():
    var = None
    val = None

class Statement():
    statement = None
