def fibonnaci_series(n):
    a=0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(a,b)    
    else:
        print(a,b,end=",")
        for i in range(1,200000):
          c=a+b
          a=b
          b=c
          print(b,end=',')
fibonnaci_series(20)            