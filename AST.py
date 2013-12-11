class Node(object):
    def __str__(self):
        return self.printTree()
        
class Const(Node):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
class Integer(Const):
    def __init__(self, value):
        Const.__init__(self, "int", value)
        
class Float(Const):
    def __init__(self, value):
        Const.__init__(self, "float", value)
        
class String(Const):
    def __init__(self, value):
        Const.__init__(self, "string", value)
        
class Variable(Node):
    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        self.value = value
        
class BinExpr(Node):
    def __init__(self, expr1, operator, expr2):
        self.expr1 = expr1
        self.operator = operator
        self.expr2 = expr2
        
class Program(Node):
    def __init__(self, declarations, fundefs, instructions):
        self.declarations = declarations
        self.fundefs = fundefs
        self.instructions = instructions
        
class Declarations(Node):
    def __init__(self, declarations, declaration):
        self.declarations = declarations
        self.declaration = declaration
        
class Declaration(Node):
    def __init__(self, type, inits, error):
        self.type = type
        self.inits = inits
        self.error = error
        
class Inits(Node):
    def __init__(self, inits, init):
        self.inits = inits
        self.init = init
        
class Init(Node):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
        
class Instructions(Node):
    def __init__(self, instructions, instruction):
        self.instructions = instructions
        self.instruction = instruction

    
class While(Node):
    def __init__(self, cond, statement):
        self.cond = cond
        self.statement = statement
        
class Return(Node):
    def __init__(self, value):
        self.value = value
        
class If(Node):
    def __init__(self, cond, statement):
        self.cond = cond
        self.statement = statement
        
class Else(Node):
    def __init__(self, statement):
        self.statement = statement
        
        
class Print(Node):
    def __init__(self, value):
        self.value = value
        
        
class RepeatUnitl(Node):
    def __init__(self, statement, cond):
        self.cond = cond
        self.statement = statement
