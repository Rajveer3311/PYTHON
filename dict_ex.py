#user to 
#  def cube(d):
#     dic={}
#     for i in range(1,d+1):
#         dic[i]=i**3
#     return dic

# print(cube(10)) 
# 
# already exist value   
def cube(d):
    dic={}
    for i in d:
        dic[i]=i**3
    return dic
num={1,2,3,4,5}
print(cube(num))    