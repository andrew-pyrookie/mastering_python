# python is and object oriented programming language
# object has properties and methods

'''
Creating a class with name MyClass with property named x
'''

class MyClass:
    x = 5

# using the class above to create objects
p1 = MyClass()
#print(p1.x)  

# The __init__ () Function

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
        
p1 = Person("John",25)

#print(p1.name)
#print(p1.age)


## The __str__ () Function
# THIS FUNCTION CONTROLS HAT SHD BE RETURNED WHEN THE CLASS OBJECT IS REPRESENTED AS A STRING

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return(f"{self.name}({self.age})")
    
p1 = Person("John", 36)

# Object Methods

class Person:
    def __init__ (self, name,age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is "+ self.name)
        
        
p1 = Person("John", 36)
p1.myfunc()


# The self Parameter
# The self parameter is a reference to the current instance of any class
# you can call it whatever you like 
class Person:
    def __init__ (mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
        
    def myfunc(abc):
        print("Hello my name is "+ abc.name)
        
p1 = Person("John", 36)
#p1.myfunc()

# modifying Object properties
p1.age = 40
print(p1.age)
    
    
# Delete Object Properties
del p1.age
#print(p1.age)