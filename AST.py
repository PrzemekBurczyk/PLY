class Node(object):
    def __str__(self):
        return self.printTree()
        
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
        self.declarations = []
        if declarations:
            self.declarations.extend(declarations.declarations)
        if declaration:
            self.declarations.append(declaration)
        
class Declaration(Node):
    def __init__(self, type, inits, error):
        self.type = type
        self.inits = inits
        self.error = error
        
class Inits(Node):
    def __init__(self, inits, init):
        self.inits = []
        if inits:
            self.inits.extend(inits.inits)
        if init:
            self.inits.append(init)
        
class Init(Node):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
        
class Instructions(Node):
    def __init__(self, instructions, instruction):
        self.instructions = []
        if instructions:
            self.instructions.extend(instructions.instructions)
        if instruction:
            self.instructions.append(instruction)

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
        self.error = error
        
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

class Condition(Node):
    pass

class Expression(Condition):
    pass

class Const(Expression):
    def __init__(self, value):
        self.value = value

class Id(Expression):
    def __init__(self, id):
        self.id = id

#class Integer(Const):
#    def __init__(self, value):
#        Const.__init__(self, "int", value)
        
#class Float(Const):
#    def __init__(self, value):
#        Const.__init__(self, "float", value)
        
#class String(Const):
#    def __init__(self, value):
#        Const.__init__(self, "string", value)

class BinExpr(Expression):
    def __init__(self, expr1, operator, expr2):
        self.expr1 = expr1
        self.operator = operator
        self.expr2 = expr2

class ExpressionInParentheses(Expression):
    def __init__(self, expression, error):
        self.expression = expression
        self.error = error

class IdWithParentheses(Expression):
    def __init__(self, id, expression_list, error):
        self.id = id
        self.expression_list = expression_list
        self.error = error

class ExpressionList(Node):
    def __init__(self, expr_list, expression):
        self.expressions = []
        if expr_list:
            self.expressions.extend(expr_list.expressions)
        if expression:    
            self.expressions.append(expression)

class FunctionDefinitions(Node):
    def __init__(self, fundef, fundefs):
        self.fundefs = []
        if fundef:
            self.fundefs.append(fundef)
        if fundefs:
            self.fundefs.extend(fundefs.fundefs)

class FunctionDefinition(Node):
    def __init__(self, type, id, arglist, compound_instr):
        self.type = type
        self.id = id
        self.arglist = arglist
        self.compound_instr = compound_instr

class ArgumentList(Node):
    def __init__(self, arg_list, arg):
        self.arg_list = []
        if arg_list:
            self.arg_list.extend(arg_list.arg_list)
        if arg:
            self.arg_list.append(arg)

class Argument(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id 

