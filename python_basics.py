#Basic Syntax
#Python Identifiers
# Used to identify a variable, function, class, module, or other object.
# Must start with a letter (A-Z to a-z)
# Can also start with an underscore.

# Rules
# Python is case-sensitive: variable, Variable, and VARIABLE are three different identifiers. 
# Identifiers can be of any length.
# Cannot use special sumboles like !, @, #, $, %, etc within identifier. 

#Multi-Line Statements
#Python allows line continuation via the backslach (\) when a single statement spans multiple lines. 
#This can make code easier to read and maintain. 

#Example:
total = 1 + \
        2 + \
        3 + \
        4 + \
        5
print(total)


#Quotations in Python
# Python supports three types of quotes to denote string literals:
# single quotes( ' )
# double quotes ( " )
# triple quotes ( ''' or """)

# This flexibiility allows you to choose the best type for your needs and to use quotes within strings without escaping them. 

# Example
word = 'word'
sentence = "This is a sentence"
paragraph = """This is a paragraph made up of multiple lines and sentences. """
print(word)
print(sentence)
print(paragraph)

# Blank Lines
# Blank Lines are not processed by Python but cna be used to separates blocks of code visually. They can make your code more readable by breaking into logical sections.

#User Input
# Python provides a built-in function input() to capture user input. This function pauses program execution and waits for user input. 

# Example
# Prompt the user to enter their name and greet them.
user_name = input("Please enter your name: ")
print("Hello, " + user_name + "!")

# Multiple Statements on a Single Line
# The semicolon (;) allows you to write multiple statements on a single line. This is typically used to condense simple statements into a single line for brevity, though it's generally discourages as it can reduce readability. 

# Example

import sys; x = "foo"; sys.stdout.write(x + '\n')


# Python Comments
# Single-line Comments
# Single-line comments are used to comment out a small piece of information or annotate a line of code. 
# You can use # symbol to add single line comment in the python code.  

# Single-line Comments
# Python does not have a specific multi-line comment features line some other languages do, but you can use consecutive single-line comments or a multi-line string (using triple quotes) that isn't assigned to a variable. 

# Example
# This is the first line of a multi-line comment.
# And this is the second line of the comment. 

"""
This is another way to create 
a multi-line comment using triple quotes.
These are often for larger descriptions or specificstions.
"""


