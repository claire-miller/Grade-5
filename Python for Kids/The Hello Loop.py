Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for x in range(0, 20)
SyntaxError: invalid syntax
>>> for x in range(0, 20):
	print('hello &s' % x)
	if x < 9:
		break

	
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    print('hello &s' % x)
TypeError: not all arguments converted during string formatting
>>> 
