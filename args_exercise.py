def to_power(num,*args):
    
    return [i**num if(args) else " hey u didt pass any argument " for i in args]



nums=[]
print(to_power(3,*nums))