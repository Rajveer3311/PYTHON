from csv import DictReader,DictWriter
with open('file.csv','r', newline='') as rf:
    with open('file4.csv','w') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['names','email','phone'])
        csv_writer.writeheader()
        for row in csv_reader:
            f,l,a=row['name'],row['email'],row['phone']
        csv_writer.writerow({'names':f,'email':l,'phone':a})