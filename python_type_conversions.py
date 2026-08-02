# Python - Type Conversions
"""
Type conversion in Python allows you to change the data type of a value to another type. 
This can be done either implicity (automatically by Python) or explicitly (manually by the programmer).
Proper understanding of both types of conversions is essential for accurate data manipulation and ensuring the correctness of program operations.

Implicit Casting - Python automatically converts one data type to another.
Explicity Casting - Developers can use functions like str(), float(), dict(), to convert one data type to another.
"""

"""
Implicit Casting (Automatic Type Conversion)

Implicit casting occurs when Python automatically converts one data type to another without any explicit insturction from the programmer.
This often happens during operations involving binary operands of different types.

"""
#Example

"""
Automatically converting an integer to a float to perform addition.
"""
# Integer and float involved in addition.
num_int = 6
num_float = 1.5

#Addition operation that triggers implicit casting.
result = num_int + num_float # Python converts integer to float

#Print the resul

print("Result: ", result) # Outputs 7.5

#The addition operation result = num_int + num_float causes num_int to be automatically converted to a float.

