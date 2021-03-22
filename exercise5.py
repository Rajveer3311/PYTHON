# def greatest_no(a,b):
#   if a>b:
#    print(a)
#   else:
#    print(b)
# x,y=input("enter first and second value:").split()      
  
# greatest_no(x,y)  
def greater(a,b):
  if a>b:
     return a
  return b
def greatest_no(a,b,c):
   bigger=greater(a,b)  
   return greater(bigger,c)
print(greatest_no(100,200,30))