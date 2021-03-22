#print 1 to 10 square
# square=[i**2 for i in range(1,11)]
# print(square)

# create negative value?
# negative=[-i for i in range(1,11)]
# print(negative)

# print 1st character of name
names=['Rajveer','Anil','Ajay','kamal']
# char=[name[0] for name in names]
# print(char)
lists=[]
for name in names:
    lists.append(name[0])
print(lists)    