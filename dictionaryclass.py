# #dictionary is a data type which store the data in key and value format

# user_dictionary={}
# print(user_dictionary,type(user_dictionary))

user_dictionary={1868:'deepa',1919:'tiger'}
print(user_dictionary,type(user_dictionary))
print("value access with key:",user_dictionary[1868],user_dictionary[1919])

# user_dictionary[1868]='ishan'#updated value
# print("value update",user_dictionary)
# user_dictionary[1869]='ishan'#inserted value
# print("value updated:",user_dictionary)


# user_dictionary.pop()
# y=user_dictionary.pop(1919)
# print("deleted:",user_dictionary,"y:",y)


# data='DEEPA'
# occurance={}
# for i in range(0,len(data)):
#     curr=data[i]
#     if (curr in 'AEIOUaeiou'):
#         if curr not in occurance:
#             occurance[curr]
#         # print('vowel',curr) =1
#         else:
#             occurance[curr]=occurance[curr]+1  #update
        
#         print(occurance)


# prices=[2,3,5,7,8,9,15,18]
# dict={}
# target=12
# for i in range(0,len(prices)):
#     dict[prices[i]]=i

# print(dict)

# for indx in range(0,len(prices)):
#     x=prices[indx]
#     y=target-x
#     print("target:",target,x,y)
#     if y in dict:
#         print('second index;',dict[y],'current index:',indx,'First and Second indx')
#         print(dict[y],'current index',i,'second value',x)
#     #target 12
#     #x+y=12

# valid anagram
# given two strings s and t ,return true if t is an anagram of s,and false otherwise
# s='anagram'
# t='nagaram'
# dict1={}
# dict2={}
# for i in range(0,len(s))

# Assignment
# 1.
# name-'Alice', age=25, city-'paris'
# name='Bob',  age=30,city='London'

# user_dictionary={'name':'Alice','age':'25','city':'paris'}
# user_dictionary2={'name':'Bob','age':'30','city':'London'}
# print(user_dictionary,type(user_dictionary))
# print(user_dictionary2,type(user_dictionary2))
# print("value access with key:",user_dictionary['name'],user_dictionary['age'],user_dictionary['city'])
# print("value access with key:",user_dictionary2['name'],user_dictionary['age'],user_dictionary['city'])

# # 2.Access Dictionary value
# d=['a': 10,'b':20],key='a'
# d=['x':5,'y':15],key='z'

# # d={'a':10,'b':20}
# # key='a'

# # print(d[key])

# d = {'x': 5, 'y': 15}
# key = 'z'

# if key in d:
#     print(d[key])
# else:
#     print("Key not found")


# numbers={10:"x",5:"V",1:"1"}
# input_number=11
# previous=0
# roman_symbols=''
# for num in numbers:
#     print(num,input_number)
#     if(input_number >= num):  #checking which number to subtract 
#         input_number = input_number-num   #updated 6-5

#         print("After substraction",input_number,numbers[num])

#         roman_symbol += numbers[num]  #adding symbol to string

#         print("symbol:",roman_symbol)


numbers={10:"x",5:"V",1:"1",4:"IV"}
input_number=14
previous=0
roman_symbols=''
for num in numbers:
    while(input_number >= num):
        print(num,input_number)
        if( input_number >= num):  #checking which number to subtract
            input_number = input_number-num  #updated 6-5


            print("after subtraction:",input_number,numbers[num])

            roman_symbol += numbers[num]  #adding symbol to string

            print("symbol:",roman_symbol)




