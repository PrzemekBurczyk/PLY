import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


class TreePrinter:

    @classmethod
    def printIndented(cls, string, level):
        print "| " * level + string

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
            TreePrinter.printIndented("DECL", indent)
            self.inits.printTree(indent + 1)

    @addToClass(AST.Inits)
    def printTree(self, indent):
        for init in self.inits:
            init.printTree(indent)
    
    @addToClass(AST.Init)
    def printTree(self, indent):
        TreePrinter.printIndented("=", indent)
        TreePrinter.printIndented(self.id, indent + 1)
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
        TreePrinter.printIndented("PRINT", indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Labeled)
    def printTree(self, indent):
        TreePrinter.printIndented(self.id + ":", indent)
        self.instruction.printTree(indent)
    
    @addToClass(AST.Assignment)
    def printTree(self, indent):
        TreePrinter.printIndented("=", indent)
        TreePrinter.printIndented(self.id, indent + 1)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Choice)
    def printTree(self, indent):
        self._if.printTree(indent)
        if self._else:
            self._else.printTree(indent)

    @addToClass(AST.If)
    def printTree(self, indent):
        TreePrinter.printIndented("IF", indent)
        self.cond.printTree(indent + 1)
        self.statement.printTree(indent + 1)

    @addToClass(AST.Else)
    def printTree(self, indent):
        TreePrinter.printIndented("ELSE", indent)
        self.statement.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent):
        TreePrinter.printIndented("WHILE", indent)
        self.cond.printTree(indent + 1)
        self.statement.printTree(indent + 1)

    @addToClass(AST.RepeatUntil)
    def printTree(self, indent):
        TreePrinter.printIndented("REPEAT", indent)
        self.statement.printTree(indent + 1)
        TreePrinter.printIndented("UNTIL", indent)
        self.cond.printTree(indent + 1) 

    @addToClass(AST.Return)
    def printTree(self, indent):
        TreePrinter.printIndented("RETURN", indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.Continue)
    def printTree(self, indent):
        TreePrinter.printIndented("CONTINUE", indent)

    @addToClass(AST.Break)
    def printTree(self, indent):
        TreePrinter.printIndented("BREAK", indent)

    @addToClass(AST.Compound)
    def printTree(self, indent):
        self.declarations.printTree(indent)
        self.instructions.printTree(indent)

    @addToClass(AST.Const)
    def printTree(self, indent):
        TreePrinter.printIndented(self.value, indent)

    @addToClass(AST.Id)
    def printTree(self, indent):
        TreePrinter.printIndented(self.id, indent)

    @addToClass(AST.BinExpr)
    def printTree(self, indent):
        TreePrinter.printIndented(self.operator, indent)
        self.expr1.printTree(indent + 1)
        self.expr2.printTree(indent + 1)

    @addToClass(AST.ExpressionInParentheses)
    def printTree(self, indent):
        self.expression.printTree(indent)
    
    @addToClass(AST.IdWithParentheses)
    def printTree(self, indent):
        TreePrinter.printIndented("FUNCALL", indent)
        TreePrinter.printIndented(self.id, indent + 1)
        self.expression_list.printTree(indent + 1)

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
        TreePrinter.printIndented("FUNDEF", indent)
        TreePrinter.printIndented(self.id, indent + 1)
        TreePrinter.printIndented("RET " + self.type, indent + 1)
        self.arglist.printTree(indent + 1)
        self.compound_instr.printTree(indent + 1)

    @addToClass(AST.ArgumentList) 
    def printTree(self, indent):
        for argument in self.arg_list:
            argument.printTree(indent)
      
    @addToClass(AST.Argument)
    def printTree(self, indent):
        TreePrinter.printIndented("ARG " + self.id, indent)
        
    # @addToClass ...
    # ...
