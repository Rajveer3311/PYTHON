# # add two num
# add=lambda a,b:a+b
# print(add(12,12))

# # multiply two num
# add=lambda a,b:a*b
# print(add(12,12))

#is even or not
# is_even=lambda a:a%2==0
# print(is_even(50))

#last char of string
last_char= lambda string : string[-1]
print(last_char('kathiya'))


# #last char of string

# def last_char(string):
#     return string[-1]
# print(last_char('kathiya'))   
# 
# # if else use
# length=lambda s:True if len(s)>5 else False
# print(length('ra')) 


# without if else
# length=lambda s: len(s)>5 
# print(length('ra')) 
num=[1,2,3,4]
# squares=list(map(lambda a:a**2,num))

# print(squares)

for a,a in enumerate(num):
    print(tuple(f"{a}:{a**2}"))   
