# def func1(array1,target):
#     for i in range(len(array1)-1):
#         for j in range(i+1,len(array1)):
#             if array1[i] + array1[j] == target:
#                print(array1[i],array1[j])
       
# array1=[3,5,2,-4,8,11]
# target=7
# # func1(array1,target)   
# 
   
# def func2(arr,target1=7):
#     return arr + arr+1 == target1
# array1=[3,5,2,-4,8,11]
# # target=2    
# function=list(map(func2,array1))
# print(function)

def twosum(arr,target=7,array=[3,5,2,-4,8,11]):
   for i in array:
        if arr + i+1 == target:
           print(arr,i+1)

array=[3,5,2,-4,8,11]
# twosum(array)
list(map(twosum,array))