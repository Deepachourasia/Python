#loops
# x=0
# for i in range(1,84):
#      if(i%2==0):
#          x+=1
#      print(i,x)

#to find factorial od no.
#5! => 1+2+3+4+5
# n=5
#'hey' =>len('hey')
#102983 => len(102983)

# for i in range(1,n+1):
#      print(i)

# n=5
# for i in range(1,n+1):
#      print(i)
#factorial programme 
#      n=6
#      a=1
# for i in range(1,n+1):
#     a=a*i
#     print(i,"a:",a)

#print factors of 10
# n=10

# for i in range (1,n+1):
#     if(n%i==0):
#         print("factors:",i)

# n=7
# count=0
# for i in range (1,n+1):
#     if(n%i==0):
#         count+=1
#         print("factors:",i,count)

       

#         if(count==2):
#             print("prime number:",i)
#         else:
#             print("not prime",i)

# n=15
# count=0
# for i in range (2,n//2):
#     if(n%i==0):
#         count+=1
#         # print("factors:",i,count)
#         if(count==0):
#             print("prime number:",n,count)
#         else:
#             print("not prime",n,count)

###
# n=15
# count=0
# for i in range (2,n//2):
#     if(n%i==0):
#         count+=1
#         print("factors:",i,count)
#         if(i==0):
#             print("prime number:",n,count)
#         else:
#             print("not prime",n,count)

# n=7
# count=0
# for i in range (1,n+1):
#     if(n%i==0):
#         count+=1
#         print("factors:",i,count)
# if(i==0):
#             print("prime number:",n,count)
#         else:
#             print("not prime",n,count)

# 1. Write a program to print all natural numbers from 1 to n. -using while
# loop
# n=10
# for i in range (1,n+1):
#      print(" Natural No." , i)

# 2. Write a program to print all natural numbers in reverse (from n to 1). –
# using while loop

# n=10
# for i in range (10,0,-1):
#     print(i)

# Write a program to print all alphabets from a to z. – using while loop
# for ch in range(ord('a'),ord('z')+1):
#     print(chr(ch))

# Write a program to print all even numbers between 1 to 100. – using
# while loop
# n=100
# for i in range (1,n+1):
#     if(i%2==0):
#         print("even no.'s",i)

# Write a program to find the sum of all odd numbers between 1 to n.
# n=100
# sum=0
# for i in range(1,n+1):
#      if(i%2!=0):
#         sum+=i
#         print("odd no.",sum)

# 6. Write a program to count the number of digits in a number.

# n=7821
# count=0
# for i in range(len(str(n))):
#     rem=n%10
#     n=n//10
#     count+=1
#     print(i,"reminder:",rem,"number:",n,"counter:",count)

# n=7821
# count=0
# for i in range(len(str(n))):
#     rem=n%10
#     n=n//10
#     count+=1
#     print(i,"reminder:",rem,"number:",n,"counter",count)

# n=7821
# for i in range(len(str(n))):
#     rem=n%10
#     n=n//10
#     count+=1
#     print(i,"reminder",rem,"number:",n,"counter:",count)


# rem=n%10
# n=n//10
# count+=1
# print(i,"reminder:",rem,"number",n,"counter",count)

# rem-n%10
# n=n//10
# count+=1
# print(i,"reminder",rem,"number",num,"counter",count)

# rem=n%10
# n=n//10
# count+=1
# print(i,"reminder",rem,"number",num,"counter",count)

# 7. Write a program to calculate the sum of digits of a number.
# n=128
# sum=0
# for digit in str(n):
#      sum += int(digit)
# print("Sum of digits =", sum)

# 8. Write a program to find the first and last digit of a number.
# 9. Write a program to find the sum of first and last digit of a number.
# 10.Write a program to enter a number and print its reverse.

# n = 124
# s = str(n)

# for i in range(len(s)):
#     if i == 0:
#         print("First Digit:", s[i])
#     if i == len(s) - 1:
#         print("Last Digit:", s[i])


# n =(input("Enter a number"))
# for i in range (len(str(n))):
#     first = n[0]
#     last = n[-1]
# print("First Digit :" , first)
# print("Last Digit :" , last) 


# 9. Write a program to find the sum of first and last digit of a number.
# sum=0
# n =input("Enter a number:")
# for i in range (len(n)):
#     first =int(n[0])
#     last = int(n[-1])
# print("first:",first,"last",last)
# sum=first+last
# print("sum:",sum)


# sum = 0
# n = input("Enter a number: ")

# for i in range(len(n)):      # loop included (exam-style)
#     first = int(n[0])
#     last = int(n[-1])

# print("first:", first, "last:", last)

# sum = first + last
# print("sum:", sum)

# 10.Write a program to enter a number and print its reverse.
# n=input("enter a number")
# rev=""
# for i in range(len(n)-1,-1,-1):
#     rev=rev+n[i]
#     print("reversed number:",rev)

# n=298
# for i in range(str(n)):
#    rem=n%10

#     if(i==0):
#         last_num=rem
#     print(i,"reminder:",rem)

# data="GOACITY"

# for ind in range(0,len(data)): #range(0,10)
#     print(ind,data(ind))

    # for char in data:
    #     print(char)

    # count how many vowels are there in jaipurcity (word) inside yourstring 
# data="JAIPURCITY"

# for ind in range(0,len(data)):# range(0,10)

#     if (data(ind)=='A'or data(ind)=='E'):
#         #if (data[ind]in 'AEIOU')
#         print(ind,data[ind])

data













    




