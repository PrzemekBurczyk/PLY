from scanner import Scanner
import AST

class Cparser(object):

    def __init__(self):
        self.scanner = Scanner()
        self.scanner.build()

    tokens = Scanner.tokens


    precedence = (
       ("nonassoc", 'IFX'),
       ("nonassoc", 'ELSE'),
       ("right", '='),
       ("left", 'OR'),
       ("left", 'AND'),
       ("left", '|'),
       ("left", '^'),
       ("left", '&'),
       ("nonassoc", '<', '>', 'EQ', 'NEQ', 'LE', 'GE'),
       ("left", 'SHL', 'SHR'),
       ("left", '+', '-'),
       ("left", '*', '/', '%'),
    )


    def p_error(self, p):
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, self.scanner.find_tok_column(p), p.type, p.value))
        else:
            print('At end of input')

    
    
    def p_program(self, p):
        """program : declarations fundefs instructions"""
        
        p[0] = AST.Program(p[1], p[2], p[3])
    
    def p_declarations(self, p):
        """declarations : declarations declaration
                        | """
                        
        if len(p) > 1:
            p[0] = AST.Declarations(p[1], p[2])
                     
    
    def p_declaration(self, p):
        """declaration : TYPE inits ';' 
                       | error ';' """
                       
        if len(p) > 3:
            p[0] = AST.Declaration(p[1], p[2], None)
        else:
            p[0] = AST.Declaration(None, None, p[1])


    def p_inits(self, p):
        """inits : inits ',' init
                 | init """

        if len(p) > 2:
            p[0] = AST.Inits(p[1], p[2])
        else:
            p[0] = AST.Inits(None, p[1])

    def p_init(self, p):
        """init : ID '=' expression """

        p[0] = AST.Init(p[1], p[3])
    
    def p_instructions(self, p):
        """instructions : instructions instruction
                        | instruction """
    
        if len(p) > 2:
            p[0] = AST.Instructions(p[1], p[2])
        else:
            p[0] = AST.Instructions(None, p[1])
    
    def p_instruction(self, p):
        """instruction : print_instr
                       | labeled_instr
                       | assignment
                       | choice_instr
                       | while_instr 
                       | repeat_instr 
                       | return_instr
                       | break_instr
                       | continue_instr
                       | compound_instr"""
    
        p[0] = p[1]
    
    def p_print_instr(self, p):
        """print_instr : PRINT expression ';'
                       | PRINT error ';' """
                       
        if type(p[2]) == AST.Expression:               
            p[0] = AST.Print(p[2], None)
        else:
            p[0] = AST.Print(None, p[2])
    
    def p_labeled_instr(self, p):
        """labeled_instr : ID ':' instruction """
    
        p[0] = AST.Labeled(p[1], p[3])
    
    def p_assignment(self, p):
        """assignment : ID '=' expression ';' """
    
        p[0] = AST.Assignment(p[1], p[3])
    
    def p_choice_instr(self, p):
        """choice_instr : IF '(' condition ')' instruction  %prec IFX
                        | IF '(' condition ')' instruction ELSE instruction
                        | IF '(' error ')' instruction  %prec IFX
                        | IF '(' error ')' instruction ELSE instruction """

        if type(p[3]) == AST.Condition:
            if p[6] == "ELSE":
                p[0] = AST.Choice(AST.If(p[3], p[5], None), AST.Else(p[7]))
            else:
                p[0] = AST.Choice(AST.If(p[3], p[5], None), None)
        else:
            if p[6] == "ELSE":
                p[0] = AST.Choice(AST.If(None, p[5], p[3]), AST.Else(p[7]))
            else:
                p[0] = AST.Choice(AST.If(None, p[5], p[3]), None)
            
    def p_while_instr(self, p):
        """while_instr : WHILE '(' condition ')' instruction
                       | WHILE '(' error ')' instruction """

        if type(p[3]) == AST.Condition:
            p[0] = AST.While(p[3], p[5], None)
        else:
            p[0] = AST.While(None, p[5], p[3])

    def p_repeat_instr(self, p):
        """repeat_instr : REPEAT instructions UNTIL condition ';' """
    
        p[0] = AST.RepeatUntil(p[2], p[4])
    
    def p_return_instr(self, p):
        """return_instr : RETURN expression ';' """
    
        p[0] = AST.Return(p[2])
    
    def p_continue_instr(self, p):
        """continue_instr : CONTINUE ';' """
    
        p[0] = AST.Continue()
    
    def p_break_instr(self, p):
        """break_instr : BREAK ';' """
    
        p[0] = AST.Break()
    
    def p_compound_instr(self, p):
        """compound_instr : '{' declarations instructions '}' """

        p[0] = AST.Compound(p[2], p[3])
    
    def p_condition(self, p):
        """condition : expression"""

        p[0] = p[1]

    def p_const(self, p):
        """const : INTEGER
                 | FLOAT
                 | STRING"""
    
        p[0] = AST.Const(p[1])
    
    def p_expression(self, p):
        """expression : const
                      | ID
                      | expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression
                      | expression '%' expression
                      | expression '|' expression
                      | expression '&' expression
                      | expression '^' expression
                      | expression AND expression
                      | expression OR expression
                      | expression SHL expression
                      | expression SHR expression
                      | expression EQ expression
                      | expression NEQ expression
                      | expression '>' expression
                      | expression '<' expression
                      | expression LE expression
                      | expression GE expression
                      | '(' expression ')'
                      | '(' error ')'
                      | ID '(' expr_list_or_empty ')'
                      | ID '(' error ')' """
    
        
    
    def p_expr_list_or_empty(self, p):
        """expr_list_or_empty : expr_list
                              | """
                              
        p[0] = AST.ExpressionList(None, None)
    
    def p_expr_list(self, p):
        """expr_list : expr_list ',' expression
                     | expression """
    
        if len(p) > 2:
            p[0] = AST.ExpressionList(p[1], p[3])
        else:
            p[0] = AST.ExpressionList(None, p[1])
    
    def p_fundefs(self, p):
        """fundefs : fundef fundefs
                   |  """
                   
        if len(p) > 1:
            p[0] = AST.FunctionDefinitions(p[1], p[2])
        else:
            p[0] = AST.FunctionDefinitions(None, None)

    def p_fundef(self, p):
        """fundef : TYPE ID '(' args_list_or_empty ')' compound_instr """
    
        p[0] = AST.FunctionDefinition(p[1], p[2], p[4], p[6])
    
    def p_args_list_or_empty(self, p):
        """args_list_or_empty : args_list
                              | """
    
        if len(p) > 1:
            p[0] = AST.ArgumentList(p[1], None)
        else:
            p[0] = AST.ArgumentList(None, None)
    
    def p_args_list(self, p):
        """args_list : args_list ',' arg 
                     | arg """
    
        if len(p) > 2:
            p[0] = AST.ArgumentList(p[1], p[3])
        else:
            p[0] = AST.ArgumentList(None, p[1])
    
    def p_arg(self, p):
        """arg : TYPE ID """
        
        p[0] = AST.Argument(p[1], p[2])