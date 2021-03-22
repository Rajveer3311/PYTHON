print(all(['True','True','True''False']))

n=[2,4,3,5]
print(any([num%2==0 for num in n]))
print(all([num%2==0 for num in n]))


#practice question
def my_sum(*args):
    if all([(type(arg)==int or type(arg)==float)for arg in args ]):
        total=0
        for num in args:
           total+=num
        return total
    else:
        return 'wrong input'
print(my_sum(1,2,3,'chaman'))        
