"""f=open("sale.txt",'w+')
print(f.write("Leads\n"))
print(f.write("Marketing\n"))
f.write("Customer\n")
f.write("Payments")"""
"""To read no of character"""
f=open("sale.txt",'r')
lcount=ccount=wcount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
    print("The number of Lines:",lcount)
    print("The number of Words:",wcount)
    print("The number of Characters:",ccount) 



"""import os
print(os.listdir())

f=open("sandeep.txt",'r')
print(f.readlines())""" 
