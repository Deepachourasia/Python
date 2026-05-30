# # function make your code readable and reusable
#def keyword  use for define the function

# # def test():
# #     a=3
# #     b=4
# #     print(a+b)

# # test()

# # print("tushar")
# # print("regex software")



# age = 18   # global variable

# def func():   # creating a function
#     x = 80    #life scope--> local scope
#     print("tushar")
#     print("regex software", x)

# func()   # run the function
# print("outside age::", age) 

# output 
#tushar
# regex software 80
# outside age:: 18


# print("---------")
# func()
# print("outside age::",age)  #2nd time run(ak baaar likha or baaar baar usko use kr rahe h by function)

#call by reference
# def test(x):


# a=12
# test(a)


#memory address id name ke function se print hoga
#based on value object refernce kaam kr rhi hai
#mutuable datatype hoga toh same memory add hoygi
# #immutable data type hoga toh diff.memoery add hoygi
# a=288
# print("a:",id(a))

# b=288
# print("b",id(b))

# c=a
# print("c:",id(c))

# mylist=[10,20]
# newlist = mylist
# print(id(mylist),id(newlist))
# newlist.append(4000)
# print(id(mylist),id(newlist),mylist,newlist)

# output: list is mutable so it's memory address not change
# 1715696154624 1715696154624
# 1715696154624 1715696154624 [10, 20, 4000] [10, 20, 4000]

# types of arguments:positional,keyword,default,var.length arg.
# Required argument(positional argument)
#we have to remember the order in this
# def test(a,b):
#     print(a,b)

# test(10,20)
# test(10,30)

#Keyword argument(In this we have to add our argument with his  key
#  or with it's parameter)
#in this we have to write name of our user

# print("below is keyword") # this is like a keyword
# test(b=10,a=30)

# def test(name,city,age):
#     print(f"name{name},city{city},age{age}")

# test('deepa','kota',22)
# test(name='deepa',age='22',city='jaipur')   

# def test(name,city,age):
#     print(f"name:{name},city:{city},age:{age}")

# test('deepa','kota',22)


#comnbined example of keyword and positional argument
# def info(name, city, age):
#     print(f"name: {name}, city: {city}, age: {age}")

# # positional
# info("deepa", "kota", 22)

# # keyword
# info(city="jaipur", age=23, name="deepa")




#Variable length argument:it is form of tuple
# In this we have to writ * 
#and keyword variable length argument ko **kwargs 
#and variable length argument ko *args
#in this it store value in the form of dictionary
# we have to give the key
#var.length arg.work like positional arg,key.len.arg. like 
#keyword argument  in this we have to define key for our value


# def user_detail(*var):
#     for i in range(0,len(var)):
#         num=var[i]
#         if(num%2==0):
#             print("even number:",num)
#     # print(var,type(var))

# # user_detail('deepa','st.pauls','rtu')
# # user_detail('deepa')

# user_detail(10,3,4,8,9,1,90,30,47,38)

#keyword variable length argument (keyword dena jrori h)
# def user_detail(**var):
#     print(var,type(var))

# user_detail(school='st.',username='deepa',college='rtu')

#Local → sirf function ke andar
# Global → har jagah
# global keyword → jab value change karni ho function ke andar se

#Return keyword

# def add_number(num):
#     global num
#     num=num+1
#     print("Inside function:",num)

# num=19 #b is global
# add_number(num) 
# print("after function:",num)


# num = 19

# def add_number():
#     global num
#     num = num + 1
#     print("Inside function:", num)

# add_number()
# print("after function:", num)

# 2-4-26

# def test(x):
#     x+1
# out=test(10)
# print("after:",out)

# def shadii(lifafa):
#     print(lifafa+100)
#     return lifafa+500

# x=shadii(1100)
# print("x value:",x )

# def prime_check():
#     num=9
#     for i in range(2,num):
#         if (num%i==0):
#             return 0
#         return 1

# z=prime_check()
# print("z value:",z)

# def func():
#     return 1
#    print(sdfhhhhhhhjjjffdkknmmolo)

# func()

#First class function

# def evenNumber():
#     print("this is a even function created by deepa")

# y=evenNumber
# print("y value::",y) # by variable assign 
# print("function::",evenNumber)

#1st prop.
# def evenNumber():
#     print("this is a even function created by deepa")

# mylist=[500,400,evenNumber()]#call in the list by ()
# print("list::",mylist)

#2nd property 
# def evenNumber():
#     print("this is a even function created by deepa")

# mylist=[500,400,evenNumber]#2nd prop.assign throgh function 
# print("list::",mylist)
# mylist[-1]()  # calling the function from list



#print use for display
# return - value ko aage bhjne ke liye

# def square(n):
#       return n+5
#       # when you want value to pass to another function use return
# def test(a,b):
#     print("a",a)
#     print("b",b)
    #   print(a,b)

# test(10,square(5))

# output: a 10
# b 10



    


