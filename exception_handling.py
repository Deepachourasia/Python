'''
try:
    print("first liner")
    x=10
    print("second liner")
    print(x[0])
    print("third liner" )
except Exception as e:
    print("found an error",e)

'''
# The finally block is used to run code no matter what happens — whether an exception occurs or not
# In Python, else is used with try-except to run code only when NO exception occurs
