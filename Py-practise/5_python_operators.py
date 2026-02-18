import operator

# List of python operators

# print("All operators in operator module:", dir(operator))

print("All operators in operator module:", operator.__all__)

# All operators in operator module: ['abs', 'add', 'and_', 'attrgetter', 'call', 'concat', 'contains', 'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul', 'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_none', 'is_not', 'is_not_none', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 'lshift', 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']

# Arithmetic Operators
a = 15  
b = 20

# first way

print("Addition:", a + b)    # Addition: 35
print("Subtraction:", a - b) # Subtraction: 5
print("Multiplication:", a * b) # Multiplication: 300
print("Division:", a / b)    # Division: 1.333333333333
print("Floor Division:", a // b) # Floor Division: 0
print("Modulus:", a % b)     # Modulus: 15

print("#" * 60)
# second way

print("Addition using operator module:", operator.add(a, b))          # Addition using operator module: 35
print("Subtraction using operator module:", operator.sub(a, b))       # Subtraction using operator module: -5
print("Multiplication using operator module:", operator.mul(a, b))    # Multiplication using operator module: 300
print("Division using operator module:", operator.truediv(a, b))      # Division using
print("Floor Division using operator module:", operator.floordiv(a, b)) # Floor Division using operator module: 0
print("Modulus using operator module:", operator.mod(a, b))           # Modulus using



# comparison Operators
x = 10
y = 20

print("\nComparison Operators:")

# first way
print("Equal to:", x == y)        # Equal to: False
print("Not Equal to:", x != y)    # Not Equal to: True
print("Greater than:", x > y)     # Greater than: False
print("Less than:", x < y)        # Less than: True
print("Greater than or Equal to:", x >= y) # Greater than or Equal to: False
print("Less than or Equal to:", x <= y)    # Less than or Equal to: True
print("#" * 60)
# second way
print("x == y:", operator.eq(x, y))  # x == y: False
print("x != y:", operator.ne(x, y))  # x != y: True
print("x > y:", operator.gt(x, y))   # x > y: False 
print("x < y:", operator.lt(x, y))   # x < y: True
print("x >= y:", operator.ge(x, y))  # x >= y: False
print("x <= y:", operator.le(x, y))  # x <= y: True


import operator

# assignment Operators

m = 5
n = 10

print("\nAssignment Operators:")
# first way
print("m =", m)
m += n
print("m += n:", m)  # m += n: 15
m -= n
print("m -= n:", m)  # m -= n: 5
m *= n
print("m *= n:", m)  # m *= n: 50
m /= n
print("m /= n:", m)  # m /= n: 5.0

# second way
m = 5  # reset m
print("#" * 60)
print("Initial m:", m)
m = operator.add(m, n)
print("after m += n:", m)  # m += n: 15
m = operator.sub(m, n)
print("after m -= n:", m)  # m -= n: 5
m = operator.mul(m, n)
print("after m *= n:", m)  # m *= n: 50
m = operator.truediv(m, n)
print("after m /= n:", m)  # m /= n: 5.0
m = operator.floordiv(m, n)
print("after m //= n:", m)  # m //= n: 0



# Logical Operators
p = True
q = False

print("\nLogical Operators:")
# first way
print("p and q:", p and q)  # p and q: False
print("p or q:", p or q)    # p or q: True
print("not p:", not p)       # not p: False
print("not q:", not q)       # not q: True

# second way
print("#" * 60)
print("operator.and_(p, q):", operator.and_(p, q))  # operator.and_(p, q): False
print("operator.or_(p, q):", operator.or_(p, q))    # operator.or_(p, q): True
print("operator.not_(p):", operator.not_(p))         # operator.not_(p): False
print("operator.not_(q):", operator.not_(q))         # operator.not_(q): True

import operator
# membership operators

list1 = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
# first way
print("3 in list1:", 3 in list1)      # 3 in list1: True
print("6 not in list1:", 6 not in list1)  # 6 not in list1: True
print("#" * 60)

# second way
print("3 in list1:", operator.contains(list1, 3))      # 3 in list1: True
print("6 in list1:", operator.contains(list1, 6))      # 6 in list1: False
print("6 not in list1:", not operator.contains(list1, 6))  # 6 not in list1: True


# identity operators

obj1 = [1, 2, 3]
obj2 = obj1

print("\nIdentity Operators:")
# first way
print("Is obj1 is obj2:", obj1 is obj2)  # Is obj1 is obj2: True
print("IS obj1 is not obj2:", obj1 is not obj2)  # obj1 is not obj2: False

# second way
print("#" * 60)
print("operator.is_(obj1, obj2):", operator.is_(obj1, obj2))  # operator.is_(obj1, obj2): True
print("operator.is_not(obj1, obj2):", operator.is_not(obj1, obj2))  # operator.is_not(obj1, obj2): False




