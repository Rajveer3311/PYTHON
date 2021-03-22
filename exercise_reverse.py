def reverse_list(l):
    element=[]
    for i in l:
        element.append(i[::-1])
    return element
string=['rajveer','kalpna','sapna','deepak','kalawati']
print(reverse_list(string))        