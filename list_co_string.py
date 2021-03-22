#list comphrension
def string_list(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float or type(i)==tuple)]
print(string_list([1,2.0,(1,2),'raaj']))    