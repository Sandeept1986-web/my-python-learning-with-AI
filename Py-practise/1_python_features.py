
print("Welcome to Python", "Using AI")


a1="Hello, Python Automation"
a2="Simple & Readable"
a3 ="*******"
print(a1, a2,  sep=a3, end="!!!!")

print("**" * 60)

import pkgutil

print("no of modules available:", len(list(pkgutil.iter_modules())))


# install packages which is not available by default using pip
# pip install requests

# interpreted - no compilation needed  

a=10
print("a =", a, "type of a:", type(a)) # a = 10 type of a: <class 'int'>
course_name = "Python Programming"
print("course_name =", course_name, "type of course_name:", type(course_name)) # course_name = Python Programming type of course_name: <class 'str'>

score=95.5
print("score =", score, "type of score:", type(score)) # score = 95.5 type of score: <class 'float'>