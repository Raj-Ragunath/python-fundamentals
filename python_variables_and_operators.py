# Python - Variables
"""

Variables are essential in any programming language. They are used to store data value. 
In Python, variables are created when you assign a value to them, and they don't require explicit declaration to reserve memory space. 
The variable is created the moment you first assign a value to it. 

"""

#Creating Variables
"""
Creating variables in Python is straightforward, you simply assign a value to a variable name.
"""

#Example:
first_name = "Raj"
age = 30
height = 5.11

#Printing Python Variables
"""
To output the value of a variable in Python, you can start with the print() function. 
This function sends the data you specify to the standard output, which is typically the terminal.
"""

#Example
print(first_name)
print(age)
print(height)

#Deleting Python Variables
"""
In Python, you can delete variables from memory using the del statement.
This can be useful when you want to free up memory or ensure that the variable is no longer accessible in later parts of your program. 
"""

#Example
player_one = "John"
player_two = "Jack"
player_three = "Jake"

print("Player 1: " + player_one)
print("Player 2: " + player_two)
print("Player 3: " + player_three)

del player_three

print()
print("Player 1: " + player_one)
print("Player 2: " + player_two)
print("Player 3 deleted.")
#print(player_three)

#Case-Sensitivity of Python Variables
"""
Python variables are case-sensitive.
This means that variables such as Age, age, and AGE are treated as distinct.
"""

#Example
Age = 29
age = 30
aGE = 31

print(Age)
print(age)
print(aGE)

#Python Variables - Multiple Assignment
"""
Python allows you to assign values to multiple variables in a single line, which can make your code cleaner and faster to write.
"""

x, y, z = 10, 20, 30

print()
print(x)
print(y)
print(z)

#Python Variables - Naming Convention
"""
When naming variables in Python, it's important to follow certain conventions and rules to ensure that your code is readable and understandable. 
These conventions alos help avoid with Python's keywords and built-in function names.
"""

"""
Rules for Naming Python Variables
1. Variable names should start with a letter or an underscore (_)
2. Variables names cannot begin with a number.
3. Variable names can only contain alphanumeric characters and underscores (A-z, 0-9, and _)
4. Variable names are case-sensitive (age, Age and AGE are different variables)
5. Avoid using Python keywords as variable names (if, else, class, etc.)
"""

#Example
#Correct variable names
username = "admin"
_user_id = 42
user2name = "guest"

#Incorrect variable names
# 2user = "guest" #SyntaxError : invalid syntax
# user-name = "admin" #SyntaxError: invalid syntax
# class = "data" #SyntaxError : invalid syntax

#Python Best Practices for Variable Names
"""
User Descriptive Names:
Variable names should be descriptive to indicate the kind of data they hold. 
For example, age is a better variable name than a, and username is a better veriable name than usrnm.

Use Lowercase for Variables:
It is common practice to use all lowercase letters for variable names, with words separated by underscores if necessary (i.e. user_age).

User CamelCase for Classes:
Class names in Python are usually written using CamelCase, where each word starts with a capital letter, without underscores (e.g., UserProfile).


By adhereing to these naming conventions and best practices, you can make your Python code more organized and easier for others (and yourself) to read and maintain.
This is especially import in collaborative enviroments or when writing publically shared code.
"""

"""
__________ END OF CHAPTER __________
"""

# Python Data Types
"""
In Python, data types are an essential concept that categorizes the type of data that can be used and manipulated within the program.
Understanding data types is crucial because it affects what kind of operations you can perform on the data.

Python is dynamically typed, which means that the type is determined at runtime and you won't need to declare it explicitly.
This flexibility allows Python to be very user-friednly and easy to work with.
"""

#Overview of Python Data Types

"""
Python's built-in data types can be categorized into several groups, each serving different purposes. 
Here is a structured table summarizing the categories and their corresponding types:

Category        Data Types
Text Type       str
Numeric Type    int, float, complex
Sequence Types  list, tuple, range
Mapping Type    dict
Set Types       set, frozenset
Boolean Type    bool
Binary Types    bytes, bytearray, memoryview
None Type        NoneType

Now, let's explore all data types in detail, beginning with Text Type and Numeric Types. 
"""

#Text Type (str)

"""
Strings in Python are sequences of characters used for storing and representing text-based information.
"""

#Example
# We will create a string variable and use basic string operations to manipulate it.

greeting = "Hello, World!"
print(greeting)

# Numeric Types (int, float, complex)
"""
Python supports several types for different kinds of mathematical operations:

Integer (int): Represents whole numbers without a fractional part, used for countable quantities. 
Floating Point Number (float): Represents real numbers with a decimal point, suitable for measurements and precise calculations.
Complex Number (complex): Consists of a real and imaginary part (denoted by "j"), used in advanced fields like engineering and scientific computation. 
"""

#Example
# We will define variables for each numeric type and demonstrate a simple calculation with each.

integer_number = 10
floating_number = 10.5
complex_number = 2 + 3j

print("Integer: ", integer_number + 5)
print("Floating: ", floating_number + 0.5)
print("Complex: ", complex_number + (1 - 2j))

# Sequence Types (list, tuple, range)
"""
Sequence types in Python include lists, tuples, and ranges. Each serves different purposes and has its own characteristics:

List (list): Lists are mutable sequences, which means their elements can be modified after creation.
Lists are ideal for storing collections of items that may need to be changed during the execution of a program.

Tuple (tuple): Tuples are immutable sequences, meaning once they are created, their contents cannot be changed. 
This is useful for fixed data sets and can provide some optimization in terms of memory usage and performance.

Range (range): The range type represents a sequence of numbers and is often used for iterating over a set number of times in loops (such as in for loops).
Range generates numbers in a specific interval (start is inclusive, end is exclusive).
"""

#Example
#Creating a list
sports_list = ['soccer', 'basketball', 'tennis']

#Creating a tuple
colors_tuple = ('red', 'blue', 'green')

#Creating a range
#number_range is generated by range(5) which includes numbers from 0 to 4. 
#The range itself is immutable and typically used for iteration.
number_range = range(5)

#Converting range to list to view it
range_list = list(number_range)

#Printing results
print("List of sports:", sports_list)
print("Tuple of colors: ", colors_tuple)
print("Range converted to list: ", range_list)

# Mapping Type (dict)
"""
Mapping types in Python store data in key-value pairs. 
The dict (dictionary) is the standard and most widely used mapping type, allowing for fast data retrieval by key, and being mutable, which means you can change, add, or delete items after the dictionary is created. 
"""

# Example
"""
We will create a simple dictionary to store user information and demonstrate how to access and modify its elements.
"""

#Creating a dictionary
user_info = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

#Accessing dictionary elements
user_name = user_info["name"] #Access the value for the key 'name'
user_age = user_info['age'] #Access the value for the key 'age'
user_city = user_info['city'] #Access the value for the key 'city'

#Printing results
print("User's Name: ", user_name)
print("User's age: ", user_age)
print("User's city: ", user_city)


#Set Types (set, frozenset)
"""
Set types in Python are collections of unique elements, meaning they do not allow duplicates. 
Python provides two types of sets: set and frozenset.
Both types are used to store unique values, but they differ in their mutability. 

Set (set): A set is mutable, meaning its contents can be changed after it is created. 
This includes adding items to the set or removing items from the set.

Frozenset (frozenset): A frozenset is immutable, meaning once it is create, its contents cannot be changed.
This makes frozensets useful as dictionary keys of another set, where immutability is necessary. 
This is because if an object can change, Python generally won't let you use it as a dictionary key or as an element of a set, because those data structures rely on their members staying unchanged after insertion. 

"""

# Example

"""
We will create a set and a frozenset to illustrate how to manipulate a set and the immutability of a frozenset.
"""

#Creating a mutable set
sports_set = {'soccer', 'basketball', 'tennis'}

#Adding an element to the set
sports_set.add('volleyball') # Adds 'voleyball' to the set. 

#Trying to add a duplicate element
sports_set.add('soccer') # 'soccer is already in the set, so it won't be added again.

#Creating an immutable frozenset
colors_frozenset = frozenset(['red', 'green', 'blue'])

#Trying to add to a frozenset
#colors_frozenset.add('purple') #AttributeError - 'frozenset' has no attribute 'add'.

print("Sports Set: ", sports_set)
print("Colors Frozenset: ", colors_frozenset)