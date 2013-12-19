import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


def printIndented(string, level):
        print "| " * level + string

class TreePrinter:


    @addToClass(AST.Node)
    def printTree(self, indent):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Program)
    def printTree(self, indent):
        self.declarations.printTree(indent)
        self.fundefs.printTree(indent)
        self.instructions.printTree(indent)

    @addToClass(AST.Declarations)
    def printTree(self, indent):
        for declaration in self.declarations:
            declaration.printTree(indent)

    @addToClass(AST.Declaration)
    def printTree(self, indent):
        if not self.error:
            printIndented("DECL", indent)
            self.inits.printTree(indent + 1)

    @addToClass(AST.Inits)
    def printTree(self, indent):
        for init in self.inits:
            init.printTree(indent)
    
    @addToClass(AST.Init)
    def printTree(self, indent):
        printIndented("=", indent)
        printIndented(self.id, indent)
        self.expression.printTree(indent + 1)
        
    @addToClass(AST.Id)
    def printTree(self, indent):
        printIndented(self.id, indent)

    @addToClass(AST.Instructions)
    def printTree(self, indent):
        for instruction in self.instructions:
            instruction.printTree(indent)
        
    @addToClass(AST.Print)
    def printTree(self, indent):
        printIndented("PRINT", indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Labeled)
    def printTree(self, indent):
        self.id.printTree(indent)
        self.instruction.printTree(indent)
    
    @addToClass(AST.Assignment)
    def printTree(self, indent):
        printIndented("=", indent)
        self.id.printTree(indent + 1)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Choice)
    def printTree(self, indent):
        self._if.printTree(indent)
        self._else.printTree(indent)

    @addToClass(AST.If)
    def printTree(self, indent):
        printIndented("IF", indent)
        self.cond.printTree(indent + 1)
        self.statement.printTree(indent + 1)

    @addToClass(AST.Else)
    def printTree(self, indent):
        printIndented("ELSE", indent)
        self.statement.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent):
        printIndented("WHILE", indent)
        self.cond.printTree(indent + 1)
        self.statement.printTree(indent + 1)

    @addToClass(AST.RepeatUntil)
    def printTree(self, indent):
        printIndented("REPEAT", indent)
        self.statement.printTree(indent + 1)
        printIndented("UNTIL", indent)
        self.condition.printTree(indent + 1) 

    @addToClass(AST.Return)
    def printTree(self, indent):
        printIndented("RETURN", indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Continue)
    def printTree(self, indent):
        printIndented("CONTINUE")

    @addToClass(AST.Break)
    def printTree(self, indent):
        printIndented("BREAK")

    @addToClass(AST.Compound)
    def printTree(self, indent):
        self.declarations.printTree(indent)
        self.instructions.printTree(indent)

    @addToClass(AST.Const)
    def printTree(self, indent):
        printIndented(self.value, indent)

    @addToClass(AST.Id)
    def printTree(self, indent):
        printIndented(self.id, indent)

    @addToClass(AST.BinExpr)
    def printTree(self, indent):
        printIndented(self.operator, indent)
        self.expr1.printTree(indent + 1)

    @addToClass(AST.ExpressionInParentheses)
    def printTree(self, indent):
        self.expression.printTree(indent)
    
    @addToClass(AST.IdWithParentheses)
    def printTree(self, indent):
        printIndented("FUNCALL", indent)
        self.id.printTree(indent + 1)
        self.expressions.printTree(indent + 1)

    @addToClass(AST.ExpressionList)
    def printTree(self, indent):
        for expression in self.expressions:
            expression.printTree(indent)
    
    @addToClass(AST.FunctionDefinitions)
    def printTree(self, indent):
        for function in self.fundefs:
            function.printTree(indent)

    @addToClass(AST.FunctionDefinition)
    def printTree(self, indent):
        printIndented("FUNDEF", indent)
        printIndented(self.id, indent + 1)
        printIndented("RET " + self.type, indent + 1)
        self.arglist.printTree(indent + 1)
        self.compound_instr.printTree(indent + 1)

    @addToClass(AST.ArgumentList) 
    def printTree(self, indent):
        for argument in self.arg_list:
            argument.printTree(indent)
      
    @addToClass(AST.Argument)
    def printTree(self, indent):
        printIndented("ARG " + self.id, indent)
        
    # @addToClass ...
    # ...
