# Global variable
global a 
a = 10  


#func : local example

def local_example():
    # local variable
    b = 20
    print("Inside local_example:")
    print("Global variable a:", a) # assessing global variable
    print("Local variable b:", b)  # assessing local variable

# func : another_function   

def another_function():
    print("Inside another_function:")
    print("Global variable a:", a) # accessing global variable
    #trying to access local variable b will raise an error
    try:
        print("Local variable b:", b)
    except NameError as e:
        print("Error:", e)

#usage 
# calling local_example
local_example()
print("-" * 40) 
# calling another_function
another_function()