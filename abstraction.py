# abstraction is a feature of oops
# where we hide the unwanted detail from the user
# to hiding the unwanted detail
#abstract method are those methods which are not implemnted
#we use @abstractmethod
# they are declared inside a class => abstract class
#to create abstract class we need to inherit abstract base class(ABC)

#from abc import ABC,abstractmethod

class RBI(ABC): #ABC => Abstract Base class, RBI is abstract class
    @abstractmethod
    def interest_rate(self):
        print(" 4% ")

class HDFC(RBI):
    def interest_rate(self):
        print("hdfc has 6%")
'''
class parent
     def paise_kama_rahe_hai


     class RBI;
         def interest():

     class HDFC
    

    class mammel:
        def legs()

    class person
       def legs
'''
# a method which is not implemented is called abstract method
#these are those method which are implemented in the child classes and to create the abstract method we need to   create abstract class
from abc import ABC, anstractmethod
#ABC => Abstract base class

class RBI(ABC):  # RBI will be abstract  class
    @abstractmethod
    def interest_rate(self):  # is a abstract method =. which is not implement
        pass

class SBI(RBI):
    name='SBI bank'
    def interest_rate(self):
        print("SBI give 10%")

sb1=SBI()
sb1.interest_rate()
sb1.display()

# create another function name self nhi doge 
# the info 1 function multiply by 100 
# Make a class in that class create a constructor and create a salary
#  instance variable also create a class variable name as organization and create a function
#  name as info . First parameter as self you used to access instance 
# and class variable access them both with the help of self create another
# function info  without self we give input
# in parameter name as percentage name as amount info function
#  with multiplying by 100 and this is static method
class tushar:
    organization='REGEX'

    def __init__(self,salary):
       self.salary=salary

    def info(self):
        print("info:",self)
        print("info:",self.organization,self.salary)

    @staticmethod
    def info2(amount):
        print("info 2:",amount)

t1=Tushar(100)
print(t1.organization,t1.salary)
t1.info()
t1.info2(245)

class Amount:
    def __init__(self,salary):
        self.salary=salary

    def __repr__(self):
        return f"Amount class have salary:{ self.salary}"

a1=Amount(50)
print(a1)

class amountnew():
    def __init__(self,salary):
        self.salary=salary

    def __repr__(self):
        return f"Amount class have salary.{self.salary}"
    
    @classmethod
    def display(cls,new):
        return Amount(new) 

print(Amount.display(99))

class Amount_2(amount):
    def __init__(self,salary):
        super().__init__(salary)

a2=amount_2(101)
print("display::",a1.display(99))
