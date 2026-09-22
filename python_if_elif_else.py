"""
Python - If ... Else

The if, elif, and else statements in Python are fundemental to controlling the flow of execution based on conditions.
These statements allow you to execute specific blocks of code depending on whether certain conditions are true or false.

Below, we'll break down how to use these constructs effectively across three sections, each focused on a different aspect of conditional execution. 
"""

"""
The if Statement

The if statement is used to execute a block of code only if a specified condition is true.

The syntax of an if statement is as follows:
if condition:
	# Block of code to execute if the condition is true. 

In the above syntax, the condition can be any expression that evaluates to either True or False.
If the condition is True, the code inside the block will execute. 
"""

# Example - If Statements
print("If Example: ")
print("x = 10. If x is greater than 5, print then x is greater than 5")
# Assign a value to x, in this case the value is 10. 
x = 10

#Checking if x is greater than 5. 
if x > 5:
	# This block of code executes only if the above condition is true. 
	print("x is greater than 5") # Output: x is greater than 5.
"""
Explanation:
x = 10 : Set the variable x to 10
if x > 5: Check if x is greater than 5
print(...): Since x is indeed greater than 5, the message "x is greater than 5" is printed to the console. 
"""

"""
The else Statement
The else statement complements the if statement and specifies a block of code to be executed if the if condition is false.

Syntax:

if condition:
	# Block of code to execute if the condition is true.
else:
	# Block of code to execute if the condition is false.

Notice that the else block only executes when the if statement's condition evaluates to False.
"""

# Example - else Statements

print()
print("Else Example")
print("x = 3. If x is greater than 5, print 'x is greater than 5', else 'print x is not greater than 5'")

x = 3

if x > 5:
	print("x is greater than 5")
else:
	print("x is not greater than 5")
"""
Explanation:
x = 3: Set the variable x to 3.
if x > 5: Check if x is greater than 5.
else: Since x is not greater than 5 (3 is not greater than 5), the else block executes.
print(...) : Prints "x is not greater than 5".
""" 

"""
The elif Statement
The elif (else if) statement allows your to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

Syntax:
if condition1:
	# Block of code to execute if condition1 evaluates to true.
elif condition2:
	# Block of code to execute if condition2 is true.
else: 
	# Block of code to execute if all conditions are false.
 
