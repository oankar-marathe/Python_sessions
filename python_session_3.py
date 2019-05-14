# def my_function():
#   print("Hello from a function")

# my_function()


# def my_function(fname, lname, age):
# 	print (fname + lname)
# 	print ("Age of" + fname + " is" + age)
# 	print (fname + "is" + age + "years old")
 
# my_function("Oankar", "marathe", 30)

# def my_function(a,b):
# 	print (a)
# 	print (b)
# 	c = a + b
# 	d = a - b
# 	return c,d

# print(my_function(40,2))ction(a,b):
# 	print (a)
# 	print (b)
# 	c = a + b
# 	d = a - b
# 	return 


#create a class & object

# class MyClass():
# 	x = 5
# 	y = "oankar"
# 	z = 'p'

# obj1 = MyClass()
# print ("Object 1 properties")
# print (obj1.x)
# print (obj1.y)
# print (obj1.z)


# obj2 = MyClass()
# print ("Object 2 properties")
# print (obj2.y)


#Constructor for a class
# class Person():

# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age


# p1 = Person("Oankar",30)
# print (p1.name)
# print (p1.age)


#Methods inside a class
class Person():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def NameFunc(self):
		print "My name is:", self.name


	def AgeFunc(self):
		print "My Age is:", self.age

p2 = Person("Oankar",30)
p2.NameFunc()
p2.AgeFunc()

# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def myfunc(self):
# 		print("Hello my name is " + self.name)

# 	def 
 
# p1 = Person("Oankar", 30)
# p1.myfunc()
