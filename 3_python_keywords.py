# import python keyword module
import keyword

# print all the keywords in python
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print("#" * 40)
# Data types keywords   
print(type(keyword.kwlist))


# No of keywords in python
print(len(keyword.kwlist))
print("#" * 40)

# is_valid_variable function
def is_valid_variable(name):
    # Block comment achieved by docstring
    """_summary_

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """

    # A valid variable name should not be a keyword
    if name in keyword.kwlist:
        return False
    # check if the name is a valid identifier
    if not name.isidentifier():
        return False    
    return True 

# test cases
test_names = ["for", "my_var", "2ndvar", "while", "valid_name", "class", "var-name"]
for name in test_names:
    print(f"'{name}' is a valid variable name") 
else:
    print(f"'{name}' is not a valid variable name")
 
"""   
#'for' is a valid variable name
#'my_var' is a valid variable name
#'2ndvar' is a valid variable name
#'while' is a valid variable name
#'valid_name' is a valid variable name
#'class' is a valid variable name
#'var-name' is a valid variable name
#'var-name' is not a valid variable name
"""

# indentation in python is very important
def example_function():
    print("This is an example function")
    if True:
        print("This line is inside if block")
    else:
        print("This line is still inside function but not in if block")   
        
    