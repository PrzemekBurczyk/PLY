import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


class TreePrinter:

    def indent(level):
        return "| " * level

    @addToClass(AST.Node)
    def printTree(self, indent):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.BinExpr)
    def printTree(self, indent):
        pass
        # ...

    # @addToClass ...
    # ...
