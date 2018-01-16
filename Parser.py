import Environment

def parse(program):
    return read_from_tokens(tokenize(program))


def tokenize(program):
    # Turns a string into a list of tokens
    return program.replace("(", " ( ").replace(")", " ) ").split()


def read_from_tokens(tokens):
    # Turns a list of tokens into the correctly nested abstract syntax tree
    if len(tokens) == 0:
        raise SyntaxError
    # Take first token
    token = tokens.pop(0)
    # Check to see that it begins with (
    if token == "(":
        token_list = list()
        # Creates a nested list for each set of parenthesis
        while tokens[0] != ")":
            token_list.append(read_from_tokens(tokens))
        tokens.pop(0)
        return token_list
    elif token == ")":
        raise SyntaxError
    else:
        # Return if it is an Atom type element
        try: return int(token)
        except ValueError:
            try: return float(token)
            except ValueError:
                return Environment.Symbol(token)

