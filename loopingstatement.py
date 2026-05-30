'''
for int i=0;i<5;i++:
     print("%d"i);


'''
#For Loop
# for i in range(1,9):
#     print("hello")

# for i in range(4,11):
#  if(i%2==0):
#     print("even",i)
#  else:
#    print("odd",i)

# for i in range(1,7):
#  if(i%2==0):
#     print("even",i)
#  if(i==4):
#    print("value is four")
#  else:
#    print("odd",i)

# for i in range(10,29):
#  if(i%2==0 and i%5==0):
#     print(i)

# for i in range(10,1):
#     if


# for i in range(1,11):
#     print(i)


# total=0
# for i in range(1,51):
   
#     print(i)
#     total=total+i
#     print("i:",i,"total:",total)

#total sum of odd numbers 
# total=0
# for i in range (1,98):
#     if(i%2!=0):
#         print(i)
#         total=total+i
#         print("i:",i,"total:",total)
# 2 3 6 divide and also calculate the number present in that
# total=0
# count=0

# for i in range(120,5):
#     if(i%2==0 and i%3==0 or i%6==0):
#         print(i)
#         total=total+i
#         count+=1
#         print("i:",i,"total:",total)
#         print("total count:",count)

# 2 ->87 and calculate the sum of all the numbers divisible by 5 and also get the 

# sum1=0
# sum2=0
# for i in range (2,88):
#     if(i%3==0):
#         print(i)
#         sum1=sum1+i
#         print("sum1:",sum1)
#     if(i%5==0):
#         print(i)
#         sum2=sum2+i
#         print("sum2:",sum2)



#somyaa code 

# FOR LOOP
# for i in range(0,5):
#     print(i)

# for i in range(1,7):
#     print(i)

# for i in range(2,6):
#     print(i)



# for i in range(1,7):
#     if(i%2==0):
#         print("Even",i)
#     else:
#         print("odd",i)



# for i in range(1,7):
#     if(i%2==0):
#         print("Even",i)
#     if(i==4):
#         print("value is four")


# for i in range (10,29):
#     if(i%2==0 and i%5==0):
#         print(i)

# for i in range (2,10,3):
#     print(i)

# for i in range (4,14,-1):
#     print(i)

# for i in range (7,1,-2):
#     print(i)


# total = 0
# for i in range(1,51):
#     print(i)
#     total = total + i
#     print("i :" , i , "Total :" ,total)

# total = 0
# for i in range (1,99):
#     if(i%2!=0):
#          print(i)
#          total = total + i
#          print("i :" , i , "Total :" ,total)



#2 3 6 divide and also calculate total number of numbers present
# total = 0
# count = 0
# for i in range (120,5):
#      if(i%2==0 and i%3==0 or (i%6==0)):
#           print(i)
#           total = total + i
#           count+=1
#           print("i :" , i , "Total :" ,total)
#           print("total count:",count)

          
#2 -> 87 and calculate the sum of all the numbers divisible by 5 & also get the sum of no. divided by 3 
# sum1 = 0  
# sum2 = 0 
# for i in range (2,88):
#      if(i%3==0):
#           print(i)
#           sum1 = sum1 + i
#           print("sum1 : ",sum1)
#      if(i%5==0):
#            print(i)
#            sum2 = sum2 + i
#            print("sum2 : ",sum2 
d = ['apple','ant','ball','bat']
d1 = {}
for word in d:
     first_ch = word[0]
     if first_ch in d1:
          d1[first_ch].append(word)
     else:
          d1[first_ch]= [word]
print(d1)          









