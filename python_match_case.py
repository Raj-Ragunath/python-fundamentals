"""
Python - Match Case

The match case statement, introduced in Python 3.10 as a structual pattern matching tool, is designed to simplify and enhance readability when dealing with complex conditional logib.
The match case statement offers a more readable and concise alternative to multiple if...elif...else statements, especially when testing a variable against multiple conditions. 

The match statement is similar to the switch case statement found in other languagges but is more powerful due to its capabilities for pattern matching. 
"""

"""
Syntax of the Match Statement
The match statement allows you to compare a value against several possible matches.
Each case can execute a block of code designed for that specific match. 

match expression:
	case pattern1:
		# Block of code for pattern 1.
	case pattern2:
		# Block of code for pattern 2.
	case _:
		# Block of code for unmatched cases (default case).

expression - This is the value that you're comparing against the patterns in each case.
pattern - These are speciic conditions or values that the expression might match. Python check the patterns in the order they are written.
_ - This is a wildcard pattern that acts are the default case, catching all values that don't match any of the previous patterns. 
"""

# Example - match Examples:
print("match Examples")
print("status code - 404, check if state code is 200, 404, or 500")
state_code = 404

match status_code:
	case 200:
		print("Success")
	case 404:
		print("Not found")
	case 500:
		print("Server Error")
	case _:
		print("Unknown status code")
