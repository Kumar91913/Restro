a='Sandeep'
output=a[ : :-1]
print(output)




a="sandeep"
b=reversed(a)
print(type(b))

a='sandeep'
b=reversed(a)
output=''.join(b)
print(output)

a='sandeep'
b=reversed(a)
for ch in b:
    print(ch)

a='kumar'
output=''
i=len(a)-1
while i>=0:
    output=output+a[i]
    i=i-1
print(output)
