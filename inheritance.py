# class ElderBrother:
#     def __init__(self,name,x,y,z):
#         self.salary=z

# eb1=ElderBrother('aman','121','')

# class StudentRegister:
#     count=0  #class variable
#     def __init__(self):
#         StudentRegister.count+=1  #changes are done for the specific
#         print("constructor called".self.count)


# s1=StudentRegister()
# s2=StudentRegister()

# class ZomatoDriver:
#     company='Zomato pvt ltd'
#     def __init__(self,name,email,ride):
#         self.name=name  #self.name="Aman"
#         self.email=email
#         self.totalRide=ride

# class ZomatoCustomer(ZomatoDriver):
#     pass

# zd1=ZomatoDriver('Aman','aman.sharma@gmail.com',100)
# print(zd1.company)
# print("rides are::",zd1.totalRide)

#to access from parent classs use super()
# class ZomatoDriver:
#     comapny='zomato pvt ltd'

#     def __init__(self,name,email,ride):
#         self.name =name
#         self.email= email
#         self.totalRide = ride

# class ZomatoCustomer(ZomatoDriver):
#     def __init__(self,x,y,z):
#         super().__init__(x,y,z)

# zc1=ZomatoCustomer('raj','raj@gmail.com',32)
# print(zc1.name)


# class A:
#     def info(self):
#         print("Info of class")

# class B(A):
#     def display(self):
#         super().info()


# b1=B()
# b1.display()

# class driver:
#      def __init__(self,name,email,trip):
#         self.name=name
#         self.email=email
#         self.trip=trip

# class customer(driver):
#     def __init__(self,name,email,trip):
#         super().__init__(name,email,trip)

# c1=customer('jussy','jussy@gmail;.com',34)
# print (c1.name)


# d1=driver('shubham','shubahm@gmail.com',189)
# print(d1.name)
# d1.display()

# c1=customer('jessy','jessy@gmail.com','76')
# print(c1.name)
# # c1.display()

# # class A:
# #     def __init__(self,a):
# #         self.a=a
# # class B(A):
# #     def __init__(self,b):
# #         self.b=b
# #         super().__init__(b)
# # class C(B):
# #     def __init__(self,c):
# #         self.c=c
# #         super().__init__(c)
# # a1=A('deepa')
# # b1=B('somya')
# # c1=c('ayushi')
# # print(a1.a)
# # print(b1.b)
# # print(c1.a)


# class A:
#     def __init__(self,a):
#         self.a=a
#         print("a constructor ",a)
# class B(A):
#     def __init__(self,b):
#         self.b=b
#         super().__init__() 
#         #A Class ka constructor call

# s = "deepa"
# occ = {}
# for i in range(0,len(s)):
#     curr=s[i]
#     if curr  not in occ:
#         occ[curr]=1
#     else:
#         occ[curr]=occ[curr]+1

#     print(i,curr,occ)

# d={'a':1,'b':2}
# new={}
# for keys,values in d.items():
#     new[values]=keys
#     print(new)
# print(new)


# class A hai jiske andr ak info method h ak b class h usme me v info method h
# c class hai vo dono ko inherit kr rhi h jisko hum bolege multiple inheritence





