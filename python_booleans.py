#Python Booleans
"""
Booleans in Python are simple yet powerful. They can hold two values: True and False.
These values enable Python to evaluate conditions or comparisons, playing a critical role in control flow and decision-making processes in programming.
"""

#Understanding Booleans
"""
In Python, a Boolean value can either be True or False. 
These values are often the result of comparison operations but can also be used directly for controlling the flow of programs with conditional statements. 
"""

# Example:

#Assigning Boolean values
is_active = True
is_registered = False

# Print the Boolean values
print("Is active", is_active)
print("Is registered: ", is_registered)


"""
Falsy Boolean Values

In Python, most objects are considered "True" when evaluated in a Boolean context.
However, certain "falsy" values are considered False. These include:
- None
- False
- Zero of any numeric type, for example 0, 0.0, 0j
- Any empty sequence, for example, '', (), []
- Any empty mapping, for example {}
"""

# Example
# This example evaluates a set of values that are "falsy", or evaluated as False in a Boolean context.

# Evaluatin falsy values
print("Printing Falsy values:")
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(''))
print(bool([]))
print(bool({}))

"""
Using Booleans in Control Structures
Booleans are crucial for controlling the flow of programs through conditional statements like if and else.
"""

# Example
"""
This example uses a Boolean variable to dictate which branch of an if-statement is executed.
"""

#Define a boolean value:
has_access = True

#Conditional execution based on the Boolean value
if has_access:
    print("Access granted.")
else:
    print("Access denied.")

"""
Booleans are fundemental in Python for making decisions within the program, enabling logical operations that depend on the truth or falsity of conditions. 
This makes programs adaptable to various scenarios based on inputs and conditions. 
"""