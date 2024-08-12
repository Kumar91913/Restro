"""
l=[10,20,30,40,50]
a=0
for value in l:
    a=a+value
print('Answer:',a)

s=[50,60,70,80,90,100]
b=1
for value in s:
    b=b+value
print('Answer:',b)
    
k=[110,120,130,140,150]
c=2
for value in k:
    c=c*value
print('Answer:',c)

m=[160,170,180,190,200]
d=6
for value in m:
    d=d+value
print('Answer:',d)

   
t=int(input("Enter the table number:"))
for i in range(1,11):
    print(t,'x',i,'=',t*i)


lower=int(input("Enter the lower number:"))
upper=int(input("Enter the upper number:"))
list=[]
for i in range(lower,upper):
    if i%5==0:
        list.append(i) 
print(list)
"""
"""
def my_function(a,b):
    print(a+b)
    print(b+a)
my_function(2,3)
"""
f=open("xyz.txt",'r')
"""
for i in length:
    print(i)
"""
lenght2=f.read()
print(len(lenght2))

word=lenght2.split()
wordcount= len(word)
print(wordcount)
















