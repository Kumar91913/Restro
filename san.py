"""import csv
with open("mysingasan.csv","w",newline='')as f:
    data=csv.writer(f)
    data.writerow(["Id","NAME","SAL","AGE"])
    num=int(input("Enter the NUMBER :"))
    for k in range(num):
        Id=int(input("Enter your Id:"))
        NAME=(input("Enter your NAME:"))
        SAL=int(input("Enter your SAL:"))
        AGE=int(input("Enter your AGE:"))
        data.writerow([Id, NAME, SAL, AGE])"""
        

import csv
with open('mysingasan.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
