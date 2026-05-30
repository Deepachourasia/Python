''' 
   feature of oops
   where we try to use methods/object to behave differently as per the 
   contact /sit:

   10+2 =>12
   "10"+"2"=>102

'''
#poly means many morphism means forms

#self
# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("dog barks")

# obj = dog()
# obj.sound()

#two methods in polymorphism
# method overloading
# 10kg => 25kg


# method overwriting

# class A:
#     def display(self):
#         print("display fucntion")

#     def display(self):
#         print("display no 2 functios")

# a1 = A()
# a1.display()
 
#  #python is a run time programming language that's why it  not support python overloading

# x=10
# x=20

# pdkkr aayge name space 
#same class me diffe.method h alg alg parameter h toh method overloading

# class parents:
#     def salary(self):
#         print("salary by doing job")

# class child(parent):
#     def salary(self):
#         print("salary by doing business")

# c1=child()
# c1.salary()


# when a parent and child have the same method same hi parameter h isse hum bolte hai method overriding

#create a class name as bank in the bank class you have constructor  name as amount
# ak or class name as bob bank, bank class have the method name as display which we print the amount

# class bank:
#      def __init__(self,amount ):
#         self.amount=amount

#      def display(self):
#         print("Bank Amount:", self.amount)

# class bobbank:
#        def amount(self,display):
#        print("salary ")

# c1= bob bank()
# c1.amount()

class add:
   def __init__(self,num1,num2):
      self.num1 =num1
      self.num2 =num2

obj = add(10,20)

print("num1:",obj.num1)
print("num2:",obj.num2)

#create a class name as Bank Account having a 
# class variable bank_name also create instance
#  variable name as account number and balance


# Method Overloading
# Same method name, different parameters
# to use this in python by Use default arguments
# Use *args

# Method Overriding
# Same method in parent and child class
# Child class changes behavior
# ✅ Supported in Python

# access modifiers
# privte public protected
# public : access anywhere
# protected : access only to child classes(_)
# private:class ke andr hi access krskte hai (__)
# abstraction is a feature of oops where we combine methods in variable together 

# class A:
#    _salary=1000 # _variable protected
#    __price=200 # private variable

#    def info(self):
#       print("info::",self.__price)

# a1=A()
# print(a1._A_price)
# a1.info()

class BankAccount:
   bank_name='HDFC bank'
   def __init__(self,accNo,balance):
      self.accno=accNo
      self.__balance=balance   #access limit <= bcz of private

   def displayBalance(self):
      return self.balance

   def add_balance(self,deposit_amount):
      self.__balance+=deposit_amount

class SavingAccount(BankAccount):
   def __init__(self,accno,balance):
         super().__init__(accNo,balance)
       
   def add_balance(self,deposit_amount):
      if(deposit _amount<25000 and deposit_amount>0):
         self._BankAccount_balance +=deposit_amount
      else:
         print("not able to deposit")

s1=SavingAccount(12912,100)
s1.add_balance(-88)
print(s1.displayBalance())

#Base class (Encapsulation)
class Account:
   def __init__(self,accNo,balance):
      self.accNo =accNo
      self.__balance = balance  # private variable __ balance => _class_balance

   def get_balance(self):  #private variable ko access
      return self.__balance

   def deposit(self,deposit_amount):
      self._balance += deposit_amount

  def withdraw(self, withdraw_amount):
      if withdraw_amount <= self.__balance
       self.__balance -= withdraw_amount
      else:
         print("Insufficient balance")

  def display(self):
   print("Account holder",self.accNo)
   print("balance:",self.__balance)

class FDAccount(Account):
   def __init__(self,accNo,balance,tenure);
   super().__init__(accNo,balance)
   self.tenure=tenure

#derived class (inheritance)
class SavingAccount(Account):

   def __init__(self,accNo,balance):
        super().__init__(accNo,balance)

   def deposit (self,deposit_amount):
      if (deposit_amount <= 30000 and deposit_amount>0):
         super().deposit(deposit_amount)

   #polymorphism
   def calculate_inheritence(self):
      return self.get_balance() =0.04

    s1= savingAccount(10293,100)
    s1.display()  

