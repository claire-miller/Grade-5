Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> another_variable = 100
>>> def variable_test2():
	first_variable = 10
	second_ variable = 20
	
SyntaxError: invalid syntax
>>> return first_variable + second_variable * another_variable
SyntaxError: 'return' outside function
>>> return first_variable * second_variable * another_variable
SyntaxError: 'return' outside function
>>> import sys
>>> print(sys.stdin.readline())



>>> 
>>> I LOve You
SyntaxError: invalid syntax
>>> I Love You
SyntaxError: invalid syntax
>>> if age >= 10 and age <= 13:
	print('What is 13 + 49 + 84 + 155 + 97? A headache!')

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    if age >= 10 and age <= 13:
NameError: name 'age' is not defined
>>> if age >= 10 and age <= 13:
	print('What is 13 + 49 + 84 + 155 + 97? A headache!')
else:
	print('Huh?')

	
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    if age >= 10 and age <= 13:
NameError: name 'age' is not defined
>>> 
