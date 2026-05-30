# "self"

# file handling is basically used to store data permanently in harddisk or ssd for future.
# open is a function
# sytax of file handling is  file_obj=open('file-path' ,'mode',)
                        #  or f=open('file name','mode') 


# f=open('new.txt')
# f.read()

# f=open('new.txt','w')  # in w mode overwrite hojati   hai chize
# f.write("python is important for interviews")
# f.close()


# f=open('new.txt')
# f.read() 
# #   ans ('python is important for interviews')

# f=open('new.txt','a')  #in append mode to add the line of previous
# f.write("so practice it daily")
# f.close()

# f=open('new.txt')
# f.read()

# f=open("file.txt","r")
# data=f.read()
# print(data)
# f.close()


# f=open("file.txt","w")
# f.write("hello")
# f.write("world")
# f.close()

# f=open('fiel.txt','w')
# f.write("hello")
# f.write('world')
# f.close()

# with open ("file.txt","w") as f:
#     f.writelines(["Hello","world"])

# with open("file.txt") as f:
#     print(f.read())

# with open("file.txt") as f:
#     data = f.read().lower()
#     count = 0
#     for ch in data:
#         if ch in "aeiou":
#             count += 1
#     print(count)

#class

# File handling is a mechanism to read/write or modify the files
# why files?
#        bcz the file are stored in the hard disk (secondary storage)
#        data on hard drive is permanently

#        open 
#        read/write
#        save and close

# open (filename,mode)
# read/write
# .close()     #or asa without with likhege toh close ki jarort hoti h

# with open(filename, mode ) as name
#   read/write      #asa likehege toh close likhnee ki jarort nhi hoti


#if we write print then it give memory address
# print(open('username.txt'))

# f= file object
# f=open('username.txt')
# print(f.read())
# f.close()

# with open('username.txt')as f:
#     print("----with new syntax---")
#     print(f.read())


#w=>write mode ye sara purana data udadegaa
# with open('username.txt',"w")as f:
#     print("----with new syntax---")
#     f.write("deepa chourasia")


# # w+. => read and write but complete data will be removed
#r+=> it is for read and write mode both ism
# with open('username.txt',"r+") as f:
#     print("----with new syntax----")
#     print(f.read())
#     f.write("ekta chourasia")

# # w+. => read and write but complete data will be removed
# with open('username.txt',"r+") as f:
#     print("----with new syntax----")
#     f.write("##")
#     print(f.tell())
#     print(f.read())

#a+ mode,wb
#read,readline,readlines()

#a+ mode is for append and read it open file for reading and appending
#wb mode (write binary) used to write binary data(images,videos,etc)
#if file exists->overwrites
# if not->creates new file
#   f=open("image.png",wb)
#   f.write(b,"binary data")
#   f.close()

# with open("file.txt","a+")as f:
# f.write("hello")

# f.seek(0)
# print(f.read())
# f.close()

# f=open("file.txt","r")
# print(f.read())
# f.close()

#read()=read entire file
# if we want to read first 5 characters then write 
# print(f.read(5))

# readline()= reads one line at a time
# f=open("file.txt","r")
# print(f.readline())
# f.close()

#it is useful for large files

# readlines()= reads all lines and return a list
# f=open("file.txt","r")
# lines=f.readlines()
# print(lines)
# f.close()

# tell()-returns current cursor position
# f =open("file.txt","r")
# print(f.tell())

# f.read(5)
# print(f.tell())
# f.close()

# seek()->moves cursor to specific position
# f.seek(offset)  #syntax

# f=open("file.txt","r")
# f.seek(3)
# print(f.read())
# f.close()

# 9-4-26
# with open('username.txt',"r") as f:
#       for x in f:
#         print("Lines::",x)


# with open("table.txt","r")as f:
#     for i in range(1,11):
#         f.write("table of {1}")

#self-practice
#count words in file

# with open("file.txt","r") as f:
#     data=f.read()
#     words=data.split()
#     print(len(words))


# #if we use split then it count words it makes list otherwise it count characters
# f=open("file.txt","r")
# data=f.read()
# words=data.split()
# print(len(words))
# f.close()


# f=open("file.txt","r")
# data=f.read().lower()

# count=0
# for ch in data:
#     if ch in "aeiou":
#         count+=1

# print("total vowels:",count)
# f.close()

# f=open("file.txt","r")
# data=f.read().lower()

# count=0
# for ch in data:
#     if  ch in "aeiou":
#         count+=1
# print("total vowels:",count)
# f.close()

# f=open("file.txt","r")
# data=f.read().lower()

# count=0
# for ch in data:
#     if ch in "aeiou":
#         count+=1
# print("total vowels:",count)
# f.close()

# f.open("file.txt","r")
# data=f.read().lower()

#function questions practice from basic
# def count_vowels(s):
#     count=0
#     for ch in s.lower():
#         if ch in "aeiou":
#             count+=1
#     return count
# print(count_vowels("python"))


# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return true

# print(is_prime(7))

# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("hello"))

# def list_sum(lst):
#     return sum(lst)

# print(list_sum([1,2,3,4]))


# def greet():
#     return "hello"

# a=greet
# print(a())

# def square(x):
#     return x*x
# def apply_func(f,value):
#     return f(value)

# print(apply_func(square,5))

# def square(x):
#     return x*x
# def apply_func(f,value):
#     return f(value)

# print(apply_func(square,5))

# def outer():
#     def inner():
#         return "Inside inner"
#     return inner

# f=outer()
# print(f())

# def my_map(func,lst):
#     result=[]
#     for i in lst:
#         result.append(func(i))
#     return result

#     print(my_map(lambda x:x*2,[1,2,3]))

    
















