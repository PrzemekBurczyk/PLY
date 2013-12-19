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

class Instruction(Node):
    pass

class Print(Instruction):
    def __init__(self, expression, error):
        self.expression = expression
        self.error = error

class Labeled(Instruction):
    def __init__(self, id, instruction):
        self.id = id
        self.instruction = instruction

class Assignment(Instruction):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

class Choice(Instruction):
    def __init__(self, _if, _else):
        self._if = _if
        self._else = _else
    
class If(Node):
    def __init__(self, cond, statement, error):
        self.cond = cond
        self.statement = statement
        self.error
        
class Else(Node):
    def __init__(self, statement):
        self.statement = statement

class While(Instruction):
    def __init__(self, cond, statement, error):
        self.cond = cond
        self.statement = statement
        self.error = error
        
class RepeatUntil(Instruction):
    def __init__(self, statement, cond):
        self.cond = cond
        self.statement = statement

class Return(Instruction):
    def __init__(self, expression):
        self.expression = expression     
        
class Continue(Instruction):
    pass

class Break(Instruction):
    pass

class Compound(Instruction):
    def __init__(self, declarations, instructions):
        self.declarations = declarations
        self.instructions = instructions

class Expression(Node):
    pass

class Condition(Expression):
    pass

class BinExpr(Expression):
    def __init__(self, expr1, operator, expr2):
        self.expr1 = expr1
        self.operator = operator
        self.expr2 = expr2

class ExpressionInParentheses(Expression):
    def __init__(self, expression):
        self.expression = expression

class IdWithParentheses(Expression):
    def __init__(self, id, expression_list):
        self.id = id
        self.expression_list = expression_list

class ExpressionList(Node):
    def __init__(self, expressions):
        self.expressions = expressions

class FunctionDefinitions(Node):
    def __init__(self, fundefs):
        self.fundefs = fundefs

class FunctionDefinition(Node):
    def __init__(self, type, id, arglist, compound_instr):
        this.type = type
        this.id = id
        this.arglist = arglist
        this.compound_instr = compound_instr

class ArgumentList(Node):
    def __init__(self, arguments):
        this.arguments = arguments

class Argument(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id 

