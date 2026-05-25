# n=28
# if(n%2==0 and n%4==0):
#     if(n%5==0):
#      print("divide by 2,4,5")
#     else:
#       print("divide by 2 and 4")

# age= 22
# sal=5000
# if(age>=18 and sal>5000):
#  sal += sal*10/100
# print(sal)

# data='@' #--A to Z 65to 90, a to z 97 to 122
# print(ord (data) )

# ch ='A'
# if(ch.isalpha()):
#     print("it is an alphabet")
# elif(ch.isdigit()):
#     print("it is a digit")
# else:
#     print("special character")

# weight=60
# height=1.7
# BMI = weight / (height ** 2)
# if(BMI < 18.5):
#     print("Underweight")
# elif(BMI >= 18.5 and BMI < 25):
#     print("Normal weight")
# elif(BMI >=25 and BMI <29.9):
#     print("Overweight")
# else:
#     print("obesity")

# n=4
# if n%2==0:
#     print("even")
# else:
#     print("odd")

#ques.2

# n=10
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")

#ques.3
# a=5
# b=9
# if a>b:
#     print("a is largest")
# elif b>a:
#     print("b is largest")
# else:
#     print("both are equal")

# a=5;b=8;c=2
# if a>b and a>c:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# else:
#     print("c is largest")
 
# n=2026
# if(n%400==0):
#     print("leap year")
# elif(n%100==0):
#     print("not a leap year")
# elif(n%4==0):
#     print("leap year")
# else:
#     print("not a leap year")

# age=22
# if(age>=18):
#     print("eligible for voting")
# else:
#     print("not eligible for voting")

# marks=89
# if marks>=90 and marks<=100:
#     print("grade A")
# elif marks>=75 and marks<=89:
#     print("grade B")
# elif marks>=60 and marks<=74:
#     print("grade c")
# else:
#     print("fail")

#Check if number is divisible by both 3 and 5.
# n=15
# if n%3==0 and n%5==0:
#     print("divisible by both ")
# else:
#     print("not divisible by both")

# n1=10
# n2=5
# op='/'
# if op=='+':
#   print(n1+n2)
# elif op=='-':
#   print(n1-n2)
# elif op=='*':
#   print(n1*n2)
# elif op=='/':
#   if n2!=0:
#     print(n1/n2)
#   else:
#     print("division by zero is not allowed")
# else:
#     print("invalid operator")

# ch= 'A'
# if ch.isalpha():
#     print("it is an alphabet")
# elif ch.isdigit():
#     print("it is a digit")
# else:
#     print("it is a special character")

# temp=35
# if temp>30:
#     print("it is hot")
# else:
#      print("it is cold")

# a=55
# if a>=40:
#     print("pass")
# else:
#     print("fail")

# a=8;b=8
# if a==b:
#     print("both are equal")
# else:
#     print("not equal")

# n=21
# if n%7==0:
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")

# n = -5 
# if n > 0:
#     if n % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")
# elif n < 0:
#     if n % 2 == 0:
#         print("Negative Even")
#     else:
#         print("Negative Odd")
# else:
#     print("Zero")

# n = -5
# if n > 0 :
#     if n % 2 == 0:
#         print("positive even")
#     else:
#         print("positive odd")

# elif n < 0:
#   if n%2 ==0:
#         print("negative even")
#   else:
#         print("negative odd")
# else:
#         print("zero")

# n=1000
# if n>0:
#     print("Eligible")
# else:
#     print("invalid principle")

# age=22
# if age<=12: 
#      print("child")
# elif age>12 and age<=18:
#     print("teenager")
# elif age>20 and age<=59:
#     print("adult")
# else:
#     print("senior ")

# password="abc123"
# if len(password)>=8:
#        print("valid")
# else:
#        print("invalid(too short)")

# n=25
# if n%2==0 or n%5==0:
#     print("yes")
# else:
#     print("no")

# day = "monday"
# if day == "saturday" or day == "sunday":
#     print("it is a weekend")
# else:
#     print("weekday")

# weight=60
# height=1.7
# BMI = weight / (height ** 2)
# if(BMI < 18.5):
#     print("Underweight")
# elif(BMI >= 18.5 and BMI < 25):
#     print("Normal weight")
# elif(BMI >=25 and BMI <29.9):
#     print("Overweight")
# else:
#     print("obesity")

#2
# units=250
# if units<=100:
#     bill=units*5
# elif units<=200:
#     bill=(100*0.5) +((units-100)*8)
# else:
#     bill=(100*5)+(100*8)+((units-200)*10)
# print("Total Bill:",bill)

#3
# storedusername="admin"
# storedpassword="password123"

# username="admin"
# password="password123"
# if username==storedusername and password==storedpassword:
#     print("login successful")
# else:
#     print("invalid username or password")

# amt=5000
# if amt>5000:
#     amt -= amt*10/100
#     print(amt)
# elif amt > 2000 and amt <=5000:
#     amt -= amt*10/100
#     print(amt)
# else:
#     print(" no discount")

#5
# a=3;b=4;c=5
# if a+b>c:
#     print("It is a valid triangle")
# elif a+c>b:
#     print("it is a valid triangle")
# elif b+c>a:
#     print("it is a valid triangle")

# else: 
#     print("it is not a valid triangle")

# a=3;b=3;c=3
# if(a==b and b==c ):
#     print("equilatral triangle")
# elif(a==b and b==c):
#     print("isosceles triangle")
# elif (a!=b and b!=c and a!=c):
#     print("scalene triangle")

# hour=12
# if hour>=5 and hour<11:
#     print("good morning")
# elif hour>=11 and hour<17:
#     print("good afternoon")
# elif hour>=17 and hour<20:
#     print("good evening")
# else:
#     print("good night")

# bal=5000,amount=1000
# if amount <=bal:
#     print("transaction successful")

# choice = 1
# a = 4
# b = 5

# if choice == 1:
#     print("Result:", a + b)

# elif choice == 2:
#     print("Result:", a - b)

# elif choice == 3:
#     print("Result:", a * b)

# elif choice == 4:
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Cannot divide by zero")

# else:
#     print("Invalid Choice")


n = 7

if n <= 1:
    print("Neither")

else:
    factors = 0

    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1

    if factors == 2:
        print("Prime")
    else:
        print("Composite")


#11
#Bank loan eligibility
# salary = 50000
# credit_score = 750
# if salary >= 30000 and credit_score >=700:
#     print("Eligible")
# else:
#     print("not eligible")

#12
# n=2
# if n>=0 and n<=2:
#     print("50")
# elif n>=2 and n<=5:
#     print("80")
# elif n>5:
#     print("120")

#13
# income = 700000
# if income <= 250000:
#     print("No Tax")
# elif income >= 250001 and income <= 500000:
#     tax = income * 5/100
#     print(tax)
# elif income >= 500001 and income <= 1000000:
#     tax = income * 20/100
#     print(tax)
# else:
#     tax = income * 30/100
#     print(tax)

#14
# age=10
# if age<12:
#     print("child discount")
# elif age>=60:
#     print("senior discount")
# else:
#     print("regular price")

#20
# n=7
# if n>=1 and n<=10:
#  print("range 1-10")
# elif n>=11 and n<=20:
#     print("range 11-20")
# else:
#     print("out of defined range")

#19
# n=600
# if n>=500:
#     print("free delivery")
# else:
#  print("delivery charges added")


#16
# marks=92
# famincome=2000
# if marks >= 85 and famincome<=30000:
#     print("eligible")
# else:
#     print("not eligible")

#17

# stock=5 
# order=3
# if(order<=stock):
#     print("confirmed")
# else:
#    print("out of stock")

#15

# hours=6
# if(hours<=2):
#     fee=hours*20
# else:
#     fee=(2*20)+(hours-2)*30
#     print("total fee:rs",fee)   

#18

# failed_attempts=2
# if(failed_attempts)>=3:
#     print("Account locked")
# else:
#     print("try again")

    








   










    









 




















  

    
   

