age=int(input("enter your age:"))
if age<=0:
    print("you can't watch")
elif 1<age<=10:
    print("ticket price is :Free")
elif 10<age<=20:
    print("ticket price is : 150")     
elif 20<age<=60:
    print("ticket price is : 200")
else:
    print("ticket price is :  250")        