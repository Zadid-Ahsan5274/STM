# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
print("---------------------Arithmetic operators---------------------")
x = 15
y = 4
print("Arithmetic operators: x + y = "+str(x+y))
print("Arithmetic operators: x - y = "+str(x-y))
print("Arithmetic operators: x * y = "+str(x*y))
print("Arithmetic operators: x / y = "+str(x/y))
print("Arithmetic operators: x % y = "+str(x%y))
print("Arithmetic operators: x // y = "+str(x//y))

# Assignment operators
print("---------------------Assignment operators---------------------")
x = 10
print(x)
x += 2
print(x)
x -= 2
print(x)
x /= 4
print(x)
x **= 4
print(x)

# Comparison operators
print("---------------------Comparison operators---------------------")
x = 10
y = 6
print("Comparison operators: x == y = "+str(x==y))
print("Comparison operators: x != y = "+str(x!=y))
print("Comparison operators: x >= y = "+str(x>=y))
print("Comparison operators: x <= y = "+str(x<=y))
print("Comparison operators: x > y = "+str(x>y))
print("Comparison operators: x < y = "+str(x<y))

# Logical operators
print("---------------------Logical operators---------------------")
x = 10
y = 4
print("Logical operators: x == y and x > y = "+str(x == y and x > y))
print("Logical operators: x == y or x > y = "+str(x == y or x > y))

# Identity operators
print("---------------------Identity operators---------------------")
x = ["rcvacademy","stm"]
y = ["rcvacademy","stm"]
print("Identity operators: x is y = "+str(x is y))
print("Identity operators: x is not y = "+str(x is not y))

# Membership operators
print("---------------------Membership operators---------------------")
x = ["rcvacademy","stm"]
y = ["rcvacademy","stm"]
print("Membership operators: 'stm' in y = "+str("stm" in y))
print("Membership operators: 'stm' not in y = "+str("stm" not in y))

# Bitwise operators
'''
& - AND
| - OR
~ - NOT
^ - XOR
'''
print("---------------------Bitwise operators---------------------")
x = 1
y = 3
print("Bitwise operators: x & y = "+str(x&y))
print("Bitwise operators: x | y = "+str(x|y))