import Evaluator, Parser

def interpreter():
    # Asks for user input for a program
    program = input("Please enter a LISP program:\n")
    # Parses the program then evaluates and prints the result
    print(Evaluator.eval(Parser.parse(program)))


interpreter()