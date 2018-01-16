import Environment


def eval(x, env=Environment.global_env):
    # Evaluates an expression based on an environment
    if isinstance(x, Environment.Symbol):
        # Returns mapping from environment if it is a symbol
        return env[x]
    elif not isinstance(x, Environment.List):
        # Returns itself if it is a number
        return x
    # Else it is an expression with an operator and elements
    op, *args = x
    if op == "if":
        # Conditional operator
        (test, conseq, alt) = args
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif op == "define":
        # Add new symbol to environment
        (symbol, exp) = args
        env[symbol] = eval(exp, env)
    else:
        # Apply operator to the arguments
        proc = eval(op, env)
        vals = [eval(arg, env) for arg in args]
        return proc(*vals)