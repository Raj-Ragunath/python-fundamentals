#Python - Operators
"""
Introduction to Python Operators

Operators in Python are special symbols that perform operations on one or more operands. 
Operands are the values or variables with which these operators are applied to produce a result.
Operators are the building blocks of Python expressions and are essential for performing calculations, making decisions, manipulating data, and more. 
Python supports a wide range of operators, each serving different purposes:

- Arithmetic Operators - Used to perform basic mathematical operations.
- Comparison (Relational) Operators - Used to compare two vvalues and determine their relationship.
- Assignment Operators - Used to assign values to variables. 
- Logical Operators - Used to combine conditional statements. 
- Bitwise Operators - Used to perform bitwise calculations on integers.
- Membership Oerators - Used to test membership / if something exists in sequences such as lists or strings. 
- Idendity Operators - Used to compare the memory locations of two objects. 

In this lesson, we will explore each type of oerator, providing definitions, usage examples, and detailed explanations of how they work in Python.
This foundational knowledge will help you write more efficient and effective Python code. 
"""

"""
Arithmetic Operators:
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and others between two numbers

The following is a table of arthmetic operators in Python:

Operator    Description         Example
+           Addition            a + b
-           Subtraction         a - b
*           Multiplication      a * b
/           Division            a / b
%           Modulus             a % b
**          Exponentiation      a ** b
//          Floor Division      a // b
"""

# Example - Arithmetic Operators
a = 10
b = 3
print(a + b) # Adds 10 and 3, outputting 13.
print(a - b) # Subtracts 3 from 10, outputting 7. 
print(a * b) # Mupliplies 10 by y, outputting 30.
print(a / b) # Divides 10 by 3, outputting the float 3.333.
print(a % b) # Finds the remainder of 10 divided by 3, and outputs 1 to the console.
print(a ** b) #Calculates 10 raised to the power of 3, outputting 1000.
print(a // b) #Performs floor division of 10 by 3, outputting 3. 