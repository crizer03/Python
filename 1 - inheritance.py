# Types of inheritance

# Single A > B
class A:
	pass
class B(A):
	pass

# Multi Level A > B > C
class A:
	pass
class B(A):
	pass
class C(B):
	pass 
	
# Hierarchical A > B, A > C
class A:
	pass
class B(A):
	pass
class C(A):
	pass 
	
# Multiple A > C, B > C
class A:
	pass
class B:
	pass
class C(A, B):
	pass 
	
# Hybrid A > B, A > C, B > D, C > D
class A:
	pass
class B(A):
	pass
class C(A):
	pass 
class D(B, C):
	pass 
 

# super() can be used in 3 ways.
# - To invoke parent class methods
# - To invoke parent class variables
# - To invoke parent class constructor

# globals() is the variables or method outside class

a, b = 15, 20
def method():
	print('Global method {}'.format('method'))
	
class A:
	a, b = 10, 20
	def __init__(self):
		print("Constructor from class A")
		
	def method(self, a, b):
		print("Method from Class A")
		
class B(A):
	a, b = 100, 200
	def __init__(self):
		print("Constructor from class B")
		super().__init__()	# Approach 1. Calls parent class constructor
		A.__init__(self)	# Approach 2. Directly specify the class
	
	def method(self, a, b):
		super().method(1, 2)					# Prints parent method
		method()								# Prints global method
		
		print(a + b)							# Local variables
		print(self.a + self.b)					# Child class variables
		print(super().a + super().b)			# Parent class variables
		print(globals()['a'] + globals()['b'])	# Global variables
		 
		
obj = B()		
obj.method(40,60)
 

































