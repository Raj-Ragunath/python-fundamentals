# Python Numbers
"""
Python supports several types of numeric data, each designed to handle different kinds of mathematical operations.
In this lesson, we'll explore four key numeric types: int, float, complex, and discuss generating random numbers using Python's random module.
"""

# Integer Type (int)
"""
Integers are whole numbers without a decimal point, which can be positive or negative.
Python's integers have unlimited precision, which means they can grow as large as the memory your program is allowed to use. 
"""

# Example
"""
This example demonstrates addition using integers.
"""

#Define integers
a = 10
b = 3

# Addition
sum = a + b

print('Sum: ', sum)

# Floating Point Type (float)
"""
Floating point numbers represent real numbers and are written with a decimal point to indicate the fractional part.
Floating point numbers are useful for representing numbers that require more precision than integers. 
"""

# Example
"""
This example shows addition with floating point numbers, highlighting potential precision issues.
"""

# Define a float
x = 0.1
y = 0.2

# Addition
total = x + y

print("Total: ", total)

# Complex Number Type (complex)
"""
Complex numbers consist of a real part and an imaginary part. 
Complex numbers are often used in scientific and engineering applications.
"""

# Example
"""
This example introduces complex numbers and extracts their real and imaginary parts.
"""

# Define a complex number
z = 1 + 2j

real_part = z.real
imaginary_part = z.imag

print("The complete complex number is: ", z)
print("The real part of the complex number is: ", real_part)
print("The imaginary part of the complex number is: ", imaginary_part)

# Random Numbers
"""
Python's random module can be used to generate random numbers, which is used in simulations, testing, and gaming. 
"""

#Example
"""
This example demonstrates how to generate a random integer within a specific range.
"""

import random

#Generate a random integer between 1 and 10.
rand_number = random.randint(1,10)

# Print the random number

print("A random number between 1 and 10 is: ", rand_number)

"""
import random : Includes Python's random module to use its functionality.
rand_number = random.randint(1,10) : Generates a random integer between 1 and 10.
print(rand_number) : Prins the random number that was generated.
"""

"""
This lesson has introduced the basic numeric types in Python, each with a practical example to illustrate their use.
These foundational concepts are essential for performing a wide range of mathematical operations in Python.
"""