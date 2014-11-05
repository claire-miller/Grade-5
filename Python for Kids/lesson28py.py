Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Girraffes(Mammals)
SyntaxError: invalid syntax
>>> class Girraffes(Mammals):
	def find_food(self):
		self.move()
		print("I've found food!")
		self.eat_food()
	def eat_leaves_from_trees(self):
		self.eat_food()
	def dance_a_jig(self):
                self.move()
		self.move()
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Girraffes(Mammals):
	def find_food(self):
		self.move()
		print("I've found food!")
		self.eat_food()
	def eat_leaves_from_trees(self):
		self.eat_food()
	def dance_a_jig(self):
                self.move()
		self.move()
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
