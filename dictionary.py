# # #method to define dictionary
# # user={'name':'rajveer','age':21}
# # print(user)
# # print(type(user))

# # #method 2nd to define dictionary
# # user1=dict(name='raj',age=24)
# # print(user1)
# # print(user1['name'])

# # #value exist in dictionary
# # if "rajveer"  in user.values():
# #     print("present")
# # else:    
# #     print("not present") 

# # #key exist in dictionary
# #     if "rajveer"  in user.values():
# #         print("present")
# #     else:    
# #         print("not present")  

#         #looping values
user={'name':'rajveer','age':21}
for i in user.values():
    print(i)           

# #looping keys
# user={'name':'rajveer','age':21}
# for i in user: :
#     print(i) 
#      #looping values
# user={'name':'rajveer','age':21}
# user=user.values()
# print(user)


# #looping keys
# user={'name':'rajveer','age':21}
# user=user.keys()
# print(user)

#add data
# user={'name':'rajveer','age':21,'fav_mov':'dil'}
# user['fav_songs']='dil','ghj'
# print(user)


#pop method
# user={'name':'rajveer','age':21,'fav_mov':'dil'}
# popped=user.pop('fav_mov')
# print(type(popped))
# print(f"popped item is {popped}")
# print(user)


#popitem method
# user={'name':'rajveer','fav_mov':'dil','age':21,}
# popped=user.popitem()
# print(type(popped))
# print(f"popped item is {popped}")
# print(user)




# #get method
# user={'name':'rajveer','age':21}
# if user.get('names'):  #none --->false
#     print("present")
# else :
#     print("not")   

#value na hone pr kuch bhi msg print kara sakte he ....
# user={'name':'rajveer','age':21}
# print(user.get('names','not found !'))

# #clear method
# user={'name':'rajveer','age':21} 
# print(user)  
# user.clear()
# print(user)   

# #copy method
# user={'name':'rajveer','age':21} 
# user1=user.copy()
# print(user1)


#update method
# user1={'name':'rajveer','age':21} 
# user2={'state':"haryana",'hobby':'youtube','name':'vikrant'}
# user1.update(user2)
# print(user1)

#fromkeys method
d=dict.fromkeys(range(1,11),'unknown')
# d=dict.fromkeys(['name','raj'],['ún','un'])
# d=dict.fromkeys('abc',"rajveer")

print(d)