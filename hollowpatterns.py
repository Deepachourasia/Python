

for i in range(4):
    for j in range(4+i):
       if j<i :
           print(" ",end=" ")
       else:
           print('*',end=' ')
    print()




# for i in range(4):
#     for j in range(6):
#         if i == 0 or i == 3 or j == 0 or j == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# for i in range(4):
#     for j in range(6):
#         if i == 0 or i == 3 or j == 0 or j == 5:
#             print("*", end="")
#         else:
#             print(" ",end="")

#         print()

# for i in range(6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()

# for i in range(6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()

# for i in range(6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()

# for i in range(6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print( )

#4
# for i in range(6):
#     for j in range(1,i+1):
#         print(chr(64+1),end=' ')
#     print( )

#5
# for i in range(6):
#     for j in range(1,i+1):
#         print(chr(67-j),end=' ')
#     print( )

# for i in range(5):
#     for j in range(69 - i, 70):
#         print(chr(j), end="")
#     print()
#        or
# for i in range(5):
#     start = ord('E') - i
#     for j in range(start, ord('E') + 1):
#         print(chr(j), end="")
#     print()


# 6.
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")

#     print(" | ",end="")

# for i in range(1,6):

#     # space for star pattern
#     for j in range(5-i):
#         print(" ", end=" ")

#     # star pattern
#     for j in range(i):
#         print("*", end=" ")

#     # separator
#     print(" | ", end="")

#     # space for number pattern
#     for j in range(5-i):
#         print(" ", end=" ")

#     # number pattern
#     for j in range(1, i+1):
#         print(j, end=" ")

#     print()

# 7.
# for i in range(1,6):
#      # spaces for number pattern
#     for j in range(5-i):
#         print(" ",end="")
#     #number pattern
#     for j in range(1,i+1):
#         print(j,end=" ")

#     print(" | ",end="")

#     #spaces for alphabet pattern
#     for j in range(5-i):
#         print(" ",end="")

#     #alphabet pattern 
#     for j in range(i):
#         print(chr(65+j),end=" ")

#     print()
    

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=5-i:
#             print(" ",end="")
#         else:
#             print(j-(5-i),end="")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if j <= 5-i:
#             print(" ", end="")
#         else:
#             print(j-(5-i), end="")
#     print()

# 6.
# for i in range(1,6):
#     for j in range(1,6):
#       if(i<=j):
#          print(j-i+1,end="")
#     else:
#         print(" ",end=" ")

#     print()



# 7.
# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ", end=" ")
    
#     for j in range(1,i+1):
#         print(j, end=" ")
    
#     print()


# 7.
# for i in range(5,0,-1):

#     # spaces
#     for j in range(5-i):
#         print(" ", end=" ")

#     # alphabets
#     for j in range(i):
#         print(chr(65+j), end=" ")

#     print()

# 8. 
# for i in range(1,6):
#     if i%2 == 1:  #for odd rows 
#         print(" ",end=" ")

#     for j in range(5):
#         print("*",end=" ")

#     print()

# 8(2).
# for i in range(5):

#     if i % 2 == 1:
#         print(" ", end=" ")

#     for j in range(1,6):
#         print(j, end=" ")

#     print()


# 8(3).
# for i in range(5):

#     if i % 2 == 1:
#         print(" ", end=" ")

#     for j in range(5):
#         print(chr(65+j), end=" ")

#     print()


#9
# rows=4

# for i in range(1,rows+1):
#     #spaces
#     for j in range(rows-i):
#         print(" ",end="")
#     #stars
#     for j in range(2*i-1):
#         print("*",end="")

#     print()

# 10.
# rows=4

# for i in range(1,rows+1):
#     #spaces
#    for j in range(rows-i):
#         print(" ",end="")
#     #stars and hollow part
#    for j in range(1,2*i):
#      if j == 1 or j == 2*i-1 or i==rows:
#         print("*",end="")
#      else:
#         print(" ",end="")

# print()

# 11.
# rows = 4

# for i in range(1, rows+1):

#     # spaces
#     for j in range(rows-i):
#         print(" ", end="")

#     # stars and hollow part
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i-1 or i == rows:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()

# 12.        *
        #  *   *
        # *      *
        #  *******
# n=5

# for i in range(1,n+1):

#     for j in range(n-1):
#         print(" ",end="")

#     for k in range(1, i+1):
#         if k==1 or k==i or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
    
#     print()

# 12.







    







