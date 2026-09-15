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
print()
print("Asssignment Operator Examples: ")
print("a = 10")
a = 10 # Assignment the value 10 to the variable a.
print("a = 10: ", a)
a += 3 # Adds the value 3 to the variable a, and assigns the new value to a.
print("a += 3: ", a)
a -= 2 # Subtracts the values 2 from the variable a and then re-assigns a to the new value.
print("a -= 2: ", a)
a *= 2 # Multiplies the value of variable a by 2 and then re-assigns a to the new value. 
print("a *= 2: ", a)
a /= 2 # Divides the value of variable a by 2 and then re-assigns a to the new value. 
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

"""
Logical Operators
Logical Operators are used to combine conditional statements in Python. 
They are fundemental in expressing compound conditions.

Operator	Description		Example
and		Logical AND		a and b
or		Logical OR		a or b
not		Logical NOT		not a
"""

#Example - Logical Operators
print()
print("Logical Operator Examples:")
print ("a = True and b = False")
a = True
b = False

print("a and b: ", a and b) # Prints False because True AND False is False.
print("a or b: ", a or b) # Prints True because a is True. True OR False results in True.
print("not a: ", not a) # Prints False because a is True and the opposite of it is False.
print("not b: ", not b) # Prints True because b is False and the opposite of it is True.

"""
Bitwise Operators
Bitwise operators are used to perform bit-level operations on integers. 
Bitwise operators manipulate individual bits of these numbers. 

Operator	Description		Example
&		Bitwise AND		a & b
|		Bitwise OR		a | b
^		Bitwise XOR		a ^ b
~		Bitwise NOT		~a
<<		Bitwise Left Shift	a << b
>>		Bitwise Right Shift	a >> b
"""

#Example - Bitwise Operators
print()
print("Bitwise Operator Examples:")
print("a = 2, b = 3")
a = 2 # 0010 in binary
b = 3 # 0011 in binary
print("a & b: ", a & b) # 0010, which is equivalent to decimal 2.
print("a | b: ", a | b) # 0011, which is equivalent to decimal 3. 
print("a ^ b: ", a ^ b) # 0001, which is equivalent to decimal 1. 
print("~a: ", ~a) # 1101, which is equivalent to decimal -3. Left most bit is 1, which signficies negative. 
#Thus, (-8 x 1) + (4 x 1) + (2 * 0) + (1 x 1) = -8 + 4 + 1 = -8 + 5 = -3.
print("~b: ", ~b) #1100, which is the equivalent of -4. -8 + 4 = -4.
print("a << 1: ", a << 1) # 0100, which is the equivalent of decimal 4.
print("a >> 1: ", a >> 1) # 0001, which is the equivalent of decimal 1.  

"""
a & b performs a bitwise AND, which results in 2 because the second bit is set in both a and b.
a | b preforms a bitwise OR, resulting in 3 because at least one of the corresponding bits is set.
a ^ b performs a bitwise XOR, resulting in 1 because only one of the corresponding bits is set in either a or b.
~a is the bitwise NOT operation, which inverts all bits of a, leading to -3 (due to two's compliment representation).
a << 1 shifts all bits in a left by one position, doubling the number to 4.
a >> 1 shifts all bits in a right by one position, halving the number to 1. 
"""

"""
Membership Operators 

Membership operators in Python are used to test whether a value or variable is found in a sequence (string, list, tuple, etc.)

Operator	Description				Example
in		True if value is in sequence.		x in y
not in		True if value is not in sequence. 	x not in y
"""

#Example - Membership Operators:
print()
print("Membership Operator Examples: ")
print("list = [1, 2, 3, 4, 5]")
my_list = [1, 2, 3, 4, 5]
three_in_list = 3 in my_list
print("3 in list: ", three_in_list) # Prints True, since 3 is indeed in the list.
six_not_in_list = 6 not in my_list
print("6 not in list: ", six_not_in_list) # Prints True, since 6 is indeed not in the list. 

"""
3 in list checks if 3 is a member of the list [1, 2, 3, 4, 5], which is true.
6 not in list checks if 6 is not a member of the list, which is true since 6 is absent.
"""

"""
Identity Operators
Identity operators compare the memory locations of two objects. 
They are used to check if objects are actually the same instance, beyond having equal value.

Operator	Description				Example
is		True if both sides are the same object.	a is b
is not		True if sides are different objects.	a is not b
"""

#Example - Identity Operators
print()
print("Identity Operators - Examples")
print("a = [1, 2, 3], b = [1, 2, 3], c = a")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a is b: ", a is b) # False. Even though the values are the same, these are two different objects. 
print("a is c: ", a is c) # True. Both a and c point to the same object. 
print("a is not b: ", a is not b) # True. Even though the values are the same, there are two different objects.

"""
a is b check if a and b refer to the same object, which is false because they are equal but not the same object.
a is c confirms that a and c refer to the same object, which is true since c is assigned to a.
a is not be checks if a and b are not the same object, which is true as they are different instances. 
"""

"""
Python Operator Precedence

Operator precedence in Python determines the order in which operations are processed. 
This can affect the outcome of expressions where multiple operators appear.
High precedence operators are executetd before lower precedence ones. 

Here's a simplified list of Python operator precedence, from highest to lowest.

Precedence	Operator Type								Operator
1		Parentheses								()	
2		Exponentiation								**
3		Unary plus, uniary minus, Bitwise NOT					+x, -x, ~x
4		Multiplicative (Multiplication, division, modulus, floor division)	*, /, &, //
5		Additive (Addition and Subtraction) 					+, -
6		Bitwise shift (Left shift, Right shift) 				<< , >>
7		Bitwise AND, OR, XOR							&, |, ^
8		Comparison Operators							==, !=, <, >, <=, >=
9		Equality (Memory locaiton / Object) 					is, is not
10		Membership (in, not in) 						in, not in
11		Logical NOT								not
12		Logical AND								and
13		Logical OR								or

"""

# Example - Operator Precedence
print()
print("Demonstrating Operator Precedence")
print("a = 10, b = 20, c = 30")
print("result = a + b * c ** 2 / 10 - 5 <= b or b % a == 0 and c > b")
a = 10
b = 20
c = 30
result = a + b * c ** 2 / 10 - 5 <= b or b % a == 0 and c > b
print("Result: ", result)

print(result)

"""
This example evaluates using Python's operator precedence rules:
c ** 2 is calculated first because ** has the highest precedence among the operators used, resulting in 900.
b * 900 is next, producing 18000.
18000 / 10 is calculated, yielding 1800.
a + 1800 gives 1810.
1810 - 5 results in 1805.
1805 <= b is evaluated (False since 1805 is not less than or equal to 20).
b % a == 0 checks if 20 is divisible by 10 without remainder (True).
c > b is True since 30 is greater than 20.
True and True is True.
False or True results in True.
"""

"""
Understanding operator precedence is essential for writing clear and correct Python code, especially in complex expressions.
Following and adhering to operator precedence ensures that you can predict and control the order of operations without excessive use of parentheses.
"""

