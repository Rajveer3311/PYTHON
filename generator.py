# def generator(n):
#     for num in range(2,n+1,2):
#         yield(num)
# for nums in generator(20):  #we can use value again..    
#     print(nums)
# for nums in generator(20):       
#     print(nums)    

# def generator(n):
#     for num in range(2,n+1,2):
#         yield(num)
# even=generator(20)        
# for nums in even:  #we can't use value again..    
#     print(nums)   
# for nums in even: 
#     print(nums)      


#generator comrehension
square=(i**2 for i in range(1,6))
print(square)
for num in square:
    print(num)   