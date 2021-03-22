from csv import reader
with open("file.csv") as f:
    csv_reader=reader(f)
    next( csv_reader)
    for i in csv_reader:
        print(i)


# from csv import reader
# with open("file.csv") as f:
#     csv_reader=f.readlines()
   
#     for i in csv_reader:
#         print(i,end='')