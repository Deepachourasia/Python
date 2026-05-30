#tuples are immutable it doesn't change once its written
# mytuple=[10,20,30,20,20,'abc']
# print(type(mytuple),mytuple[-1:-3])
# print(mytuple.count(20))
# print(mytuple.index('abc'))


# tea_types=("Black","Green","Oolong")
# tea_types
# ('Black','Green','Oolong')
# tea_types[0]
# more_tea=("Herbal","Earl Greay")
# all_tea=more_tea + tea_types
# all_tea

# s="("
# is_bracket=""

# for indx in range(0,len(s)):
#     current=s[indx]
#     print(indx,current)
#     if(current=='('or current=="[" or current=="{"):
#         is_bracket=current 
#     elif(current==")" and "("== is_bracket):
#         print("valid")
#     elif(current=="]" and "["=is_bracket):
#         print("valid:",is_bracket,current)
#     elif(current=="]" and "["=is_bracket):
#         print("valid:",is_bracket,current)
#     else:
#         print("invalid")
#         break