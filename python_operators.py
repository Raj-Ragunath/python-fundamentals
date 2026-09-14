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

"""
Comparison (Relatioal) Operators:
Comparison operators are used to compare two values, outputting a Boolean value based on whether the comparison is true or false. 

Operator    Description         Example
==          Equal to            a == b  
!=          Not equal to        a != b
<	    Greater than 	a > b
< 	    Less than		a < b
>=	    Greater than or equal to 	a >= b
<=	    Less than or equal to 	a <= b
"""

#Example
print("Comparison (Relational) Operator Examples:")
print("a = 10, b = 3")
a = 10
b = 3
print("Does a = b? ", a == b)
print("Is a not equal to b? ", a != b)
print("Is a greater than b? ", a > b)
print("Is a less than b? ", a < b)
print("Is a greater than or equal to be? ", a >= b)
print("Is a less than or equal to be? ", a <= b)

"""
Assignment Operators
Assignment operators in Python are used to assign values to variables, often simplifying code by combining standard operations with an assignment.

The following is a table of assignment operators in Python:

Operator	Description			Example
=		Simple assignment		a = b
+= 		Addition and assignment		a += b
-=		Subtraction and assignment	a -= b
*=		Multiplication and assignment	a *= b
/=		Division and assignment		a /= b
%=		Modulus and assignment		a %= b
**=		Exponent and assignment		a **= b
//		Floor division and assignment	a //= b
&=		Bitwise AND and assignment	a &= b
|= 		Bitwise OR and assignment	a |= b
^= 		Bitwise XOR and assignment	a ^= b
<<= 		Leftshift and assignment	a <<= b
>>= 		Right shift and assignment	a >>= b
"""

# Examples - Assignment Operators
print("Asssignment Operator Examples: ")
print("a = 10")
a = 10 # Assignment the value 10 to the variable a.
print("a = 10: ", a)
a += 3 # Adds the value 3 to the variable a, and assigns the new value to a.
print("a += 3: ", a)
a -= 2
print("a -= 2: ", a)
a *= 2
print("a *= 2: ", a)
a /= 2
print("a /= 2: ", a)
a %= 4
print("a %= 4: ", a)
a **= 2
print("a **= 2: ", a)
a //= 2
print("a //= 2: ", a)
a = int(a)
a &= 3
print("a &= 3: ", a)
a |= 8
print("a |= 8: ", a)
a ^= 6
print("a ^= 6: ", a)
a <<= 1
print("a <<= 1: ", a)
a >>= 2
print("a >>= 2: ", a)

print("Final value of a: ", a)

