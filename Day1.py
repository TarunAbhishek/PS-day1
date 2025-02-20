#Variables
x = 10
name = "Python"
print(x, name)

#Conditional Statements
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Loops
#For loop
for i in range(5):
    print(i)
#While loop
x = 0
while x < 5:
    print(x)
    x += 1

#Functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Tarun"))

#Jump Statements
#Break statement
for i in range(10):
    if i == 5:
        break
    print(i)
#Continue Statement
for i in range(10):
    if i == 5:
        continue
    print(i)

#Indentation
if True:
    print("Indented properly")
    
#if True:
#print("Incorrect indentation")  # ❌ Will give an error

#Operations
#Arithmetic
a = 10
b = 5
print(a + b, a - b, a * b, a / b, a % b, a ** b)
#Comparison
print(5 == 5, 5 != 5, 5 > 5,
      5 < 5, 5 >= 5, 5 <= 5)
#Logical
x = True
y = False
print(x and y, x or y, not x)




