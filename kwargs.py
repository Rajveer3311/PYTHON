def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
names={'name':'kamal','age':21}        
func(**names)