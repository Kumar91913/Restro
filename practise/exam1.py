f=open("bcg.txt",'r')
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(lines)
    words=line.split()
    wcount=wcount+len(words)
    print("The number of Lines:",lcount)
    print("The number of Words:",wcount)
    print("The number of Characters:",ccount) 

