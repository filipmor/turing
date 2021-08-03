"""
Simple Lisp Scheme interpreter fulfilling the Turing Completeness program criteria

General overview:
- a Scheme Symbol is implemented as a Python string
- a Scheme List is implemented as a Python list
- a Scheme Number is implemented as a Python numeric (int or float)

"""
from parse import *
from evaluate import *

if __name__ == '__main__':
    prompt = 'LispScheme> '
    global_env = Environment()
    while True:
        input_expression = input(prompt)
        try:
            if input_expression == 'exit': 
                break
            # Parse the input
            parsed_expression = parse(input_expression)
            # Evaluate the input
            response = evaluate(parsed_expression, global_env)
            if response is not None:
                print(response)
        except Exception as e:
            raise SyntaxError