class Laptop:
    count_=0
    def __init__(self,name,model,price):
        self.count_+=1
        print('!! laptop details !!')
        self.name=name
        self.model=model
        self.price=price

lp=Laptop('Dell','Inspiron 3584',40000) 
print(lp.name)
print(lp.count_)
