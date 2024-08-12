"""Writing a data to a file"""

"""with open("Encrypt.txt",'w') as f:
    f.write("data1\n")
    f.write("data2\n")
    f.write("data3\n")
    f.write("data4\n")"""

"""Reading a data a from a file"""

"""with open("Encrypt.txt",'r') as f:
    print(f.readlines()[-2])
    """
"""Reading number of lines of a file    

with open("Encrypt.txt",'r') as f:
    lcount=0
    for line in f:
        lcount = lcount +1
        
    print("The number of lines:",lcount)"""
    
"""Read number of charcter from a file

with open("Encrypt.txt",'r') as f:
    ccount=0
    for line in f:
        ccount=ccount+len(line)

    print("The number of charcter:",ccount)"""

"""Read the number of words from a file"""

with open("Encrypt.txt",'r') as f:
    wcount=0
    for line in f:
        words=line.split()
        wcount=wcount+len(words)

    print("The number of words:",words)
        
        













    
