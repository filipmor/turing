def parenthesize(tokenized_expression):
    """
    Recursive function splitting the tokenized expression based on the scope of parenthesis

    @type tokenized_expression: list
    @param tokenized_expression: the list of a Scheme expression parts

    @return: nested list with expression tokens mapped appropriately
    """
    token = tokenized_expression.pop(0)
    if token == "(":
        token_list = []            
        for i in range(len(tokenized_expression)):
            if tokenized_expression[0] == ')':
                break
            token_list.append(parenthesize(tokenized_expression))
        # Remove '(' from the end of the expression
        tokenized_expression.pop(0)
        return token_list
    elif token == ")":
        raise SyntaxError("Unexpected '('")
    else:
        return categorize(token)

def categorize(token):
    """
    Categorize token based on a Python to Scheme relation: 
    - a Scheme Symbol is implemented as a Python string
    - a Scheme List is implemented as a Python list
    - a Scheme Number is implemented as a Python numerc (int or float)

    @type token: str
    @param token: An expression token to be converted into appropriate type

    @return: obj
    """
    try: 
        return float(token)
    except ValueError:
        try: 
            return int(token)
        except ValueError:
            return str(token)


def tokenize(expression):
    """
    Function tokenizing expressions based on a Scheme parenthesis syntax
    The spaces around parenthesis are added to separate characters

    @type expression: str
    @param expression: a Python expression to be translated into a Scheme

    @return: the list of a Scheme expression parts
    """
    return expression.replace('(',' ( ').replace(')',' ) ').split()

def parse(expression):
    """
    Main function responsible for parsing Python expressions into a Scheme expression
    Tokenize expression and read from tokens accordingly to Scheme
    
    @type expression: str
    @param expression: a Python expression to be translated into a Scheme

    @return: the expression in a Scheme
    """
    tokenized_expression = tokenize(expression)
    if len(tokenized_expression) == 0:
        raise SyntaxError("Error: A Scheme expression is empty")
    return parenthesize(tokenized_expression)