# Python Inheritance:
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''

#Create a Parent Class:
#Any class can be a parent class, so the syntax is the same as creating any other class:
#e.g:Create a class named Person, with firstname and lastname properties, and a printname method:
class person:
    def __init__(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname

    def printname(self):
        print(self.fname,self.lname)

x = person("parikshan","shahi")
x.printname()

#Create a Child Class:
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
#e.g:Create a class named Student, which will inherit the properties and methods from the Person class:
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class students(person):
        pass
x = students("pariskhan","shahi")
x.printname()

# Add the __init__() Function
'''
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.'''
#e.g:Add the __init__() function to the Student class:

class person:
     def __init__(self,fname,lname):
          self.firstname = fname
          self.lastname = lname

     def printname(self):
          print(self.firstname,self.lastname)

class student(person):
     def __init__(self,fname,lname):
          person.__init__(self,fname,lname)

x = student("parikshan","shahi")
x.printname()
# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

#Use the super() Function:
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
#e.g:
class person:
     def __init__(self,fname,lname):
          self.firstname = fname
          self.lastname = lname

     def printname(self):
          print(self.firstname,self.lastname)

class manager(person):
     def __init__(self,fname,lname):
          super().__init__(fname,lname)
        
x = manager("hintake","thakuri")
x.printname()
#By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.

# Add Properties:
class student:
     def __init__(self,fname,lname):
          self.firstname = fname
          self.lastname = lname

     def printname(self):
          print(self.firstname,self.lastname)
class person(student):
     def __init__(self,fname,lname):
          super().__init__(fname,lname)
          self.grauationyear = 2024
x = person("parikshan","shahi")
x.printname()
print(x.grauationyear)
# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:
#Add a year parameter, and pass the correct year when creating objects:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

# Add Methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()
#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

