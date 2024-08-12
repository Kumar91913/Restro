f=open("table.txt","w")
with open("table.txt",'w')as f:
    for k in range(1,51):
        f.write("\n")
        for j in range(1,11):
            f.writelines(['{}*{}={}\n'.format(k,j,k*j)])
    
       
f=open("table.txt","r")
table=f.readlines()[-1]
print(table)
f.close()
