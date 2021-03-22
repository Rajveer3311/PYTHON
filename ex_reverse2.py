def reverse_list(l):
    reverse2=[]
    for i in range(len(l)):
        r=l.pop()
        reverse2.append(r)
    return reverse2
numbers=list(range(1,6))   
print(numbers)
print(reverse_list(numbers))     

# def reverse_list(l):
#     l.reverse()
#     return l

# num=list(range(1,6))    
# print(reverse_list(num))