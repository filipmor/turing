from environment import *

statements = Statements()

class Procedure(object):
    """
    The Procedure class for the user defined, custom variables and functions
    """
    def __init__(self, custom_variables, custom_values):
        """
        The constructor of the Procedure class 
        
        @type custom_variables: tuple 
        @param custom_variables: tuple with variable and function names defined by user


        @type custom_values: tuple
        @param custom_values: tuple with values corresponding to the variable and function names defined by user
        """
        self.custom_variables = custom_variables
        self.custom_values = custom_values
                            
    def __call__(self, *args): 
        return evaluate(self.custom_values, Environment(self.custom_variables, args))

def evaluate(expression, environment):
    """
    Main function responsible for the evaluation of parsed Python expressions, according to the Lisp Scheme statements and operators
    Current version covers three statements: define, if, lambda
    As well as conditions for the type of Lisp Scheme data (string, numeric) and user defined variables, functions

    @type expression: list
    @param expression: list of parsed and tokenized Lisp Scheme expressions

    @type environment: dict
    @param environment: Environment object (based on dict)

    """
    if isinstance(expression, str):
        # Check for the Lisp Scheme Symbol
        return environment[expression]
    elif isinstance(expression, (int, float)):
        # Check for the Lisp Scheme Numeric
        return expression
    elif expression[0] == statements['define']:
        # Definition of variables, functions; recursively calls itself to process inner part
        (_, value, rest) = expression
        environment[value] = evaluate(rest, environment)
    elif expression[0] == statements['if']:
        # Conditional statement
        (_, test, consequence, alternative) = expression
        result_expression = (consequence if evaluate(test, environment) else alternative)
        return evaluate(result_expression, environment)
    elif expression[0] == statements['lambda']:
        # Lambda statement creating custom functions
        (_, custom_variables, custom_values) = expression
        return Procedure(custom_variables, custom_values)
    else:
        # Update of the environment for the user defined variables/functions and execution of this custom object
        procedure = evaluate(expression[0], environment)
        args = [evaluate(exp, environment) for exp in expression[1:]]
        return procedure(*args)
