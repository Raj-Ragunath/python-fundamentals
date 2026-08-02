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

"""
Explicity Casting (Manual Type Conversion)

Explicity casting involves manually converting the data type of a value using Python's built-in functions such as int(), float(), and str().
This section focuses on converting data type explcitly to ensure proper data manipulation when automatic conversions are not available or suitable.
"""

"""
Integer to String Conversion - str()

To combine numbers with strings or to output numbers are part of strings in display messages, you need to convert integers to strings. 
THis is done using the str() function.
"""

# Example

#Using str() to convert an integer to a string

# Integer to string conversion
num = 10
num_str = str(num) # Convert integer to string.

# Print the converted value.
print("String: ", num_str) # Outputs: String: 10

# num_str = str(mum) uses str() function to convert the integer to a string. 

"""
String to Integer Conversion

When dealing with input or data that involves numerical values stored as strings, such as user inputs or data read from a file, you may need to convert these strings back to integers for mathematical operations.

The int() function is used for this purpose. 
"""

# Example

# Converting a string to an integer using int()

#String to Integer Conversion
num_str = "20"
num = int(num_str) # Converts a string to integer.

#Print the converted value
print("Integer: ", num)
print("Type: ", type(num))

# num = int(num_str) converts the string to an integer using the int() function.

"""
Integer to Float Conversion

There are situations, especially in calculations involving division or precise measurements, where converting integers to floats is necessary.
The float() function is used to convert integers (or other compatible types) to floating-point numbers.

"""

# Example

# Converting an integer to a float using float().

# Integer to float conversion
num_int = 4
num_float = float(num_int) # Convert integer to float.

# Print the converted value.
print("Float: ", num_float)
print("Type: ", type(num_float))

# num_float = float(num_int) converts the integer to a float, ensuring it has a decimal point. 

"""
Boolean to Integer Conversion

Boolean in Python can also be converted to integers for numerical computations where True is equivalent to 1 and False is equivalent to 0.

"""

# Example:
# Converting booleans to integers.

# Boolean to integer conversion.
true_value = True
false_value = False
true_int = int(true_value) # Converts True to 1.
false_int = int(false_value) # Converts False to 0. 

#Print the converted values
print("Integer from True: ", true_int) # Outputs: Integer from True: 1.
print("Type: ", type(true_int))
print("Integer from False: ", false_int) # Outputs: Integer from False: 0.
print("Type: ", type(false_int))

# true_int = int(true_value) and false_int = int(false_valuse) converts the booleans to their respective integer equivalents.

# The print statements confirm the conversion results, showing 1 for True and 0 for False. 

"""
Data Type Conversion Functions

Python provides several built-in functions that allow explicit conversion between different data types.
Thes functions are essential tools in Python programming, enabling manual data conversions where automatic conversions are not appropriate or possible.
Below is a table summarizing the main type conversion functions available in Python:
"""

"""
Function        Description     Example Usage
int()           Converts a number or string to an integer, if possible.                 int(2.8) -> 2
float()         Converts a numbre or string to a floating point number.                 float("3.5") -> 2.5
str()           Converts an object to a string representation.
bool()          Converts an object to a Boolean value, using standard truth testing.
complex()       Converts a number or string to a complex number.
list()          Converts an iterable to a list.
tuple()         Converts an iterable to a tuple.
set()           Converts an iterable to a set (removing duplicate elements).
dict()          Creates a dictionary from a sequence of key-value pairs.
bin()           Converts an integer to a binary string.
hex()           Converts an integer to a hexadeimal string.
oct()           Converts an integer to a octal string. 

These functions are instrumental for ensuring that data types match expected formats in functions and operations, thereby preventing type errors and steamlinin code execution.
"""

