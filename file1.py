with open('file2.txt','a') as f:
    f.write('hello')
# # print(f.tell())
# print(f.read())
# f.seek(0)
# print(f.read())
# print(f.tell())
# print(f.closed)
# print(f.name)
# print(f.readlines())
# for i in f:
#     print(i,end='')

with open('file2.txt','r') as rf:
    with open('file3.txt','w') as wf:
        wf.write(rf.read())
        