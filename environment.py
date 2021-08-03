import operator as op
import math

class Environment(dict):
    """
    The Environment class containing the allowed operations in Lisp Scheme.
    The Environment is based on math and operator, native Python packages. 
    However, it also allows to add user defined variables and functions to the scope.
    """
    def __init__(self, custom_variables=(), custom_values=()):
        """
        Constructor of the Environment class
        @type custom_variables: tuple
        @param custom_variables: tuple with variable and function names defined by user

        @type custom_values: tuple
        @param custom_values: tuple with values corresponding to the variable and function names defined by user

        """
        self.update(zip(custom_variables, custom_values))
        # Updates the environment with Python packages containing mathematical operations
        self.update(vars(math))
        self.update({
            '+':op.add, 
            '-':op.sub, 
            '*':op.mul, 
            '/':op.truediv, 
            '>':op.gt, 
            '<':op.lt, 
            '>=':op.ge, 
            '<=':op.le, 
            '=':op.eq, 
            'abs':     abs,
            'append':  op.add,  
            'apply':   'apply',
            'begin':   lambda *x: x[-1],
            'car':     lambda x: x[0],
            'cdr':     lambda x: x[1:], 
            'cons':    lambda x,y: [x] + y,
            'eq?':     op.is_, 
            'equal?':  op.eq, 
            'length':  len, 
            'list':    lambda *x: list(x), 
            'list?':   lambda x: isinstance(x,list), 
            'map':     map,
            'max':     max,
            'min':     min,
            'not':     op.not_,
            'null?':   lambda x: x == [], 
            'number?': lambda x: isinstance(x, (int, float)),   
            'procedure?': callable,
            'round':   round,
            'symbol?': lambda x: isinstance(x, str),
        })
        

class Statements(dict):
    """
    The Statements class containing dictionary of allowed in Lisp Scheme statements
    """
    def __init__(self):
        """
        The constructor of the Statements class; current version is minimalistic but should still allow
        for the language to be considered as Turing Complete
        """
        self.update({
            'if': 'if',
            'define': 'define',
            'lambda': 'lambda'
        })
