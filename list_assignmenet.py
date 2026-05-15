#1. sum of list elements
# lst=[1,2,3,4,5]
# sum=0
# for i in range(0,len(lst)):
#     sum=sum+lst[i]
# print("sum=",sum)


# 2.find the largest element in a list
# mylist=[3,7,2,9,1]
# x=mylist[0]
# for i in range(0,len(mylist)):
#     if(mylist[i]>x):
#         x=mylist[i]
#     print(mylist[i],x)

# 3.count even numbers in a list
# mylist=[1,2,3,4,5,6]
# even_lst=[]
# count=0
# for i in range(0,len(mylist)):
#     if(mylist[i]%2==0):#to find even no.
#         even_list.append(mylist[i])
#         count += 1
#         print("even",i,mylist[i],even_lst)

# print("total even numbers:",count)

# or

# mylist = [1,2,3,4,5,6]
# count = 0

# for num in mylist:
#     if num % 2 == 0:
#         count += 1

# print("Total even numbers:", count)

# 5.find the largest element in a list
# mylist=[3,7,2,9,1]
# x=mylist[0]
# Smax=0
# for i in range(0,len(mylist)):
#     if[mylist[i]>x]:
#         Smax=x
#         x=mylist[i]
#     elif(mylist[i]>Smax):
#         Smax=mylist[i]
    
#     print("values:",mylist[i],"max:",x,Smax)


# 6.remove duplicates from a list (preserve order)
# lst=[1,2,2,3,1,4]
# for i in range(0,len(lst)):
#     print(lst[i],lst)
#     lst.pop()
    #    or

# i=0
# while(i<len(lst)):
#     ("before pop",i,lst)
#     mylist.pop()
#     print("after pop",i,mylist[i])
#     i+=1

# 6.
# Har element ke aage check karo
# agar same mile → remove kar do
# mylst=[1,2,2,3,1,4]
# i=0
# while i < len(mylst):
#     j=i+1
#     while j < len(mylst):
#       if mylst[i]==mylst[j]:
#         mylst.pop(j) #remove duplicate
#       else:
#         j += 1

#     i+=1
# print(mylst)

# or


# lst=[1,2,2,3,1,4]
# i=len(lst)-1
# while i>=0:
#     if lst(i) in lst[0:i]:
#        lst.pop(i)
#     i-=1
# print(lst)

# 7.Find all elements greater than the average
# Hint: Slice the list at position k and rearrange the parts.
# lst = [1,2,3,4,10]
# new_list=[]
# sum=0
# average=0
# for ind in range(0,len(lst)):
#     sum=sum+lst[ind]
#     average=sum/len(lst)
# print("avg",average)
# for num in lst:
#     if num >=average:
#         new_list.append(num)
# print(new_list)

# 8.Rotate a list to the left by k positions
# Hint: Slice the list at position k and rearrange the parts.
# lst=[1,2,3,4,5]
# k=2
# lst=lst[k: ]+lst[ :k]
# print(lst)

# 9.find the longest consecutive sequence in a list
# lst=[1,2,3,10,11,12,13]
# lst.sort()
# print(lst)
# length=1
# curr=1
# for i in range(1,len(lst)):
#     if lst[i] == lst[i-1]:
#         curr+=1
#     else:
#         curr=1
#     if curr>length:
#          length=curr
#     print(length)

# 10.Group consecutive duplicates into sublists
# lst=[1,1,2,3,3,3,4]
# result=[]
# curr=[lst[0]]   # 1
# for i in range(1,len(lst)):  # 1 ->lst[i]=1
#     if curr[-1]==lst[i]:  
#         curr.append(lst[i])
#     else:
#         result.append(curr)
#         curr=(lst[i])
#     result.append(curr)  #group complete 
#     print(result)

# 11.flatten a 2D list into a 1D list
# flatten means sublist ke elements ko ek hi list me daalna toh first ak me hi daalna hai 
# toh add krna pdega add krne ke liye append use kro
# lst=[[1,2],[3,4],[5,6]]
# result=[]
# for row in range(0,len(lst)):
#     for ele in lst[row]:
#         result.append(ele)
# print(result)

# 12.find the frequency of each element
# output:[(1,1),(2,2),(3,3)]

# lst=[1,2,2,3,3,3]
# visited=[]
# for i in range(len(lst)):
#     if lst[i] in visited:
#         continue
#     count=0
#     for j in range(len(lst)):
#         if lst[i] == lst[j]:
#             count+=1
#         print(lst[i],count)
#         visited.append(lst[i])



# lst = [1,2,2,3,3,3]
# visit = []
# for i in range(len(lst)):
#     if lst[i] in visit:
#         continue
#     count=0
#     for j in range(len(lst)):
#         if lst[i] == lst[j]:
#             count+=1
#     print(lst[i],count)
#     visit.append(lst[i])

# 13.Merge two sorted lists into one sorted list
# output:[1,2,3,4,5,6]

# lst1=[1,3,5]
# lst2=[2,4,6]
# merge_lst=[]
# i=j=0

# while i < len(lst1) and j < len(lst2):
#       if lst1[i]<lst2[j]:
#         merge_lst.append(lst1[i])
#         i+=1
#       else:
#         merge_lst.append(lst2[j])
#         j+=1
# #add remaining elements
# while i < len(lst1):
#     merge_lst.append(lst1[i])
#     i+=1
# while j < len(lst2):
#     merge_lst.append(lst2[j])
#     j+=1

# print(merge_lst)

# lst1=[1,3,5]
# lst2=[2,4,6]
# i=0
# j=0
# res=[]
# while i<len(lst1) and j<len(lst2):
#     if lst1[i] < lst2[j]:
#         res.append(lst1[i])
#         i+=1
#     else:
#         res.append(lst2[j])
#         j+=1
# res.extend(lst1[i :])
# res.extend(lst2[j :])
# print(res)

# 14.check if a list is a pallindrome 
# output:True
# lst=[1,2,3,2,1]
# i=0
# j=len(lst)-1
# while i<j:
#     if lst[i]!=lst[j]:
#         print("Not pallindrome")
#         break
#     i+=1
#     j-=1

# else:
#         print("pallindrome")

# 15.find all pairs that sum to a target value
# lst=[1,2,3,4,5]
# target=5
# res=[]
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             res.append((lst[i],lst[j]))
# print(res)

# #'(',')'
# result=[]
# for ch in range:
#     if ch == '('or'{'or'[':
#         result.append(ch)

# s="("
# is_bracket=""

# for indx in range(0,len(s)):
#     current=s[indx]
#     print(indx,current)
#     if(current=='('or current=="[" or current=="{"):
#         is_bracket=current 
#     elif(current==")" and "("= is_bracket):
#         print("valid")
#     elif(current=="]" and "["=is_bracket):
#         print("valid:",is_bracket,current)
#     elif(current=="]" and "["=is_bracket):
#         print("valid:",is_bracket,current)
#     else:
#         print("invalid")
#         break

        























